"""
    File name: test_devops_mensaje.py
    Author: Angel Quingaluisa
    Date created: 04/06/2019
    Python Version: 3.6
"""

# Cargamos el módulo unittest
from django.test import TestCase, Client
from rest_framework import status
from rest_framework.test import APITestCase

from devops_env import logica_negocio
from devops_env.settings import API_KEY_SECRET


class MensageTest(TestCase):

    def test_enviar_mensaje(self):
        """
        Probar el metodo que envia un mensaje
        :return:
        """
        mensaje = {}
        mensaje['message'] = "This is a test"
        mensaje['to'] = "Angel Quingaluisa"
        mensaje['from'] = "Rita Asturia"
        mensaje['timeToLifeSec'] = "45"
        resultado = logica_negocio.leerMensaje(mensaje)
        print("respuesta:" + resultado)

        self.assertIn('Hello', resultado)


class testStatus(APITestCase):
    def test_http200(self):
        """Valida que exista respuesta  en el http 200"""
        client = Client()

        url = '/Devops'
        data = {"message": "This is a test", "to": "Juan Perez", "from": "Rita Asturia", "timeToLifeSec": 45}

        response = client.post(url, data, format='json',HTTP_X_PARSE_REST_API_KEY= API_KEY_SECRET)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_http403(self):
        client = Client()
        """
        Valida que la autentificaciones este correcta
        """
        url = '/Devops'
        data = {"message": "This is a test", "to": "Juan Perez", "from": "Rita Asturia", "timeToLifeSec": 45}

        response = client.post(url, data, format='json',HTTP_X_PARSE_REST_API_KEY= API_KEY_SECRET)
        self.assertNotEqual(response.status_code, status.HTTP_403_FORBIDDEN)

"""
    File name: test_devops_mensaje.py
    Author: Angel Quingaluisa
    Date created: 04/06/2019
    Python Version: 3.6
"""

# Cargamos el módulo unittest
from django.test import TestCase, Client

from devops_env import logica_negocio


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

        self.assertIn('Hello',resultado)

"""
    File name: views.py
    Author: Angel Quingaluisa
    Date created: 03/06/2019
    Python Version: 3.6
"""
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from devops_env import logica_negocio
from rest_framework import status

from devops_env.permissions import Check_API_KEY_Auth


@api_view(['POST', 'GET'])
@permission_classes((Check_API_KEY_Auth, ))
def leerMensaje(request):
    """
    Retorna los datos iniciales necesarios para perfil menu
    :return:
    """
    try:
        resultado = logica_negocio.leerMensaje(request.data)
        return Response(resultado, status=status.HTTP_200_OK)
    except Exception as  ex:
        return Response(data="ERROR", status=status.HTTP_400_BAD_REQUEST)

"""
    File name: logica_negocio.py
    Author: Angel Quingaluisa
    Date created: 03/06/2019
    Python Version: 3.6
"""

from rest_framework.response import Response


def leerMensaje(mensaje):
    try:
        # mensaje.get('message')
        # mensaje.get('to')
        # mensaje.get('from')
        # mensaje.get('timeToLifeSec')
        return 'Hello  ss' + str(mensaje.get('to')) + ' your message will be send.'
    except Exception as  ex:
        raise ex


"""
    Validar los permisos de acceso al microservicio
    File name: logica_negocio.py
    Author: Angel Quingaluisa
    Date created: 03/06/2019
    Python Version: 3.6
"""
from rest_framework.permissions import BasePermission

from devops_env import settings


class Check_API_KEY_Auth(BasePermission):
    message = 'No tiene autorizacion para utilzar el  microservicio'
    """
    Clase para  implementar si tiene permisos para el api key
    """
    def has_permission(self, request, view):
        """
        Validar si tiene permiso   con el api key
        :param request:
        :param view:
        :return:
        """
        # API_KEY should be in request headers to authenticate requests
        api_key_secret = request.META.get('HTTP_X_PARSE_REST_API_KEY')
        return api_key_secret == settings.API_KEY_SECRET
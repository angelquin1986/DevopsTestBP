"""
    Registro  de la url del api rest que de despliega
    File name: url.py
    Author: Angel Quingaluisa
    Date created: 03/06/2019
    Python Version: 3.6
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from devops_env import views

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    path('devops', views.leerMensaje),
]

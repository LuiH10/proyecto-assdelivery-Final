# configuracion/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.configuracion_usuario, name='configuracion_usuario'),
]


from django.urls import path
from .views import login_view, recuperar_contrasena, registro_view, resetear_contrasena

urlpatterns = [
    path('recuperar/', recuperar_contrasena, name='recuperar_contrasena'),
    path('resetear/<str:correo>/', resetear_contrasena, name='resetear_contrasena'),
    path('registro/', registro_view, name='registro'),
]

from django.urls import path
from .views import (
    configuracion_usuario,
    eliminar_consultor,
    eliminar_consultor_directo
)

urlpatterns = [
    path('', configuracion_usuario, name='configuracion_usuario'),
    path('eliminar_consultor/<int:user_id>/', eliminar_consultor, name='eliminar_consultor'),
    path('eliminar-consultor-directo/', eliminar_consultor_directo, name='eliminar_consultor_directo'),
]


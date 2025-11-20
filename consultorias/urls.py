from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_consultorias, name='lista_consultorias'),
    path('editar/<int:consultoria_id>/', views.editar_consultoria, name='editar_consultoria'),
    path('eliminar/<int:consultoria_id>/', views.eliminar_consultoria, name='eliminar_consultoria'),
]


from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_clientes, name='lista_clientes'),
    path('eliminar/<int:cliente_id>/', views.eliminar_cliente, name='eliminar_cliente'),
    path('cambiar-estado/<int:cliente_id>/', views.cambiar_estado_cliente, name='cambiar_estado_cliente'),
    path('editar/<int:cliente_id>/', views.editar_cliente, name='editar_cliente'),
]


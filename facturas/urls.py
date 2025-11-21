from django.urls import path
from . import views
from .views import factura_pdf

urlpatterns = [
    path('', views.lista_facturas, name='lista_facturas'),
    path('crear/', views.crear_factura, name='crear_factura'),
    path('eliminar/<int:factura_id>/', views.eliminar_factura, name='eliminar_factura'),
    path('pdf/<int:factura_id>/', factura_pdf, name='factura_pdf'),
    path('editar/<int:id>/', views.editar_factura, name='editar_factura'),  # <-- ESTA ES LA QUE FALTABA
]









from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_facturas, name='lista_facturas'),
    path('crear/', views.crear_factura, name='crear_factura'),
    path('eliminar/<int:factura_id>/', views.eliminar_factura, name='eliminar_factura'),
    path('pdf/<int:factura_id>/', views.generar_pdf_factura, name='generar_pdf_factura'),
    path('editar/<int:id>/', views.editar_factura, name='editar_factura'),  # <-- ESTA ES LA QUE FALTABA
]




from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_reportes, name='lista_reportes'),
    path('pdf/<int:reporte_id>/', views.reporte_pdf, name='reporte_pdf'),
    path('excel/<int:reporte_id>/', views.reporte_excel, name='reporte_excel'),
    path('eliminar/<int:reporte_id>/', views.eliminar_reporte, name='eliminar_reporte'),
    path('editar/<int:id>/', views.editar_reporte, name='editar_reporte'),
]





from django.contrib import admin
from .models import Consultoria

@admin.register(Consultoria)
class ConsultoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'fecha', 'estado')
    list_filter = ('estado', 'fecha')
    search_fields = ('cliente__nombre', 'descripcion')

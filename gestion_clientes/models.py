from django.db import models
from django.contrib.auth.models import User  # para el campo "asignado"

class Cliente(models.Model):
    asignado = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    nombre = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)
    estado = models.CharField(
        max_length=20,
        choices=[
            ('activo', 'Activo'),
            ('inactivo', 'Inactivo'),
            ('pendiente', 'Pendiente')
        ],
        default='activo'
    )

    def __str__(self):
        return f"{self.nombre} ({self.empresa})"


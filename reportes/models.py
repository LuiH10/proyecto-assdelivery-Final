from django.db import models
from django.contrib.auth.models import User

class Reporte(models.Model):
    consultor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    descripcion = models.TextField()
    fecha_emision = models.DateField(auto_now_add=True)
    estado = models.CharField(
        max_length=20,
        choices=[
            ('pendiente', 'Pendiente'),
            ('en_proceso', 'En proceso'),
            ('completado', 'Completado'),
        ],
        default='pendiente'
    )

    def __str__(self):
        return f"Reporte #{self.id} - {self.consultor} ({self.estado})"


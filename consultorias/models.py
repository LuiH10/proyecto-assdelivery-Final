from django.db import models
from gestion_clientes.models import Cliente

class Consultoria(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    descripcion = models.TextField()
    estado = models.CharField(
        max_length=20,
        choices=[
            ('pendiente', 'Pendiente'),
            ('en_proceso', 'En proceso'),
            ('finalizada', 'Finalizada')
        ],
        default='pendiente'
    )

    def __str__(self):
        return f"Consultoría #{self.id} - {self.cliente.nombre}"


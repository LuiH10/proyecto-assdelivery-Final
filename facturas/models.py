from django.db import models
from gestion_clientes.models import Cliente # type: ignore

class Factura(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='facturas')
    fecha_emision = models.DateField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(
        max_length=20,
        choices=[
            ('pendiente', 'Pendiente'),
            ('pagada', 'Pagada'),
            ('vencida', 'Vencida'),
        ],
        default='pendiente'
    )

    def __str__(self):
        return f"Factura #{self.id} - {self.cliente.nombre} (${self.total})"

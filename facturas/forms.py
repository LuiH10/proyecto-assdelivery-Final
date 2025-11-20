from django import forms
from .models import Factura
from gestion_clientes.models import Cliente

class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = ['cliente', 'total', 'estado']  # NO 'fecha_emision' (es auto_now_add)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Ordena y asegura que aparezcan todos los clientes en el <select>
        self.fields['cliente'].queryset = Cliente.objects.all().order_by('nombre')
        self.fields['cliente'].label = 'Cliente'
        self.fields['total'].label = 'Monto total'
        self.fields['estado'].label = 'Estado'

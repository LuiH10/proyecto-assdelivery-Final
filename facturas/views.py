from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template.loader import render_to_string
from .models import Factura
from .forms import FacturaForm
from weasyprint import HTML
import tempfile
from django.http import HttpResponse
from django.template.loader import render_to_string
from io import BytesIO
from django.shortcuts import get_object_or_404
from .models import Factura

# 🔹 Mostrar lista de facturas
from gestion_clientes.models import Cliente  # 👈 importar

def lista_facturas(request):
    facturas = Factura.objects.all().order_by('id')
    clientes = Cliente.objects.all()  # 👈 agregar
    return render(request, 'facturas/lista_facturas.html', {
        'facturas': facturas,
        'clientes': clientes  # 👈 agregar al contexto
    })



# 🔹 Crear nueva factura
def crear_factura(request):
    if request.method == 'POST':
        form = FacturaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_facturas')
    else:
        form = FacturaForm()
    return render(request, 'facturas/crear_factura.html', {'form': form})


# 🔹 Eliminar factura
def eliminar_factura(request, factura_id):
    factura = get_object_or_404(Factura, id=factura_id)
    factura.delete()
    return redirect('lista_facturas')




def generar_pdf_factura(request, factura_id):
    factura = get_object_or_404(Factura, id=factura_id)
    html_string = render_to_string('facturas/factura_pdf.html', {'factura': factura})

    # Generar el PDF directamente en memoria (sin usar archivos temporales)
    pdf_file = BytesIO()
    HTML(string=html_string).write_pdf(pdf_file)
    pdf_file.seek(0)

    response = HttpResponse(pdf_file.read(), content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename=factura_{factura.id}.pdf'
    return response

from django.contrib import messages  # IMPORTANTE
from django.shortcuts import render, redirect, get_object_or_404
from .models import Factura, Cliente

def editar_factura(request, id):
    factura = get_object_or_404(Factura, id=id)
    if request.method == 'POST':
        cliente_id = request.POST.get('cliente')
        total = request.POST.get('total')
        estado = request.POST.get('estado')

        factura.cliente_id = cliente_id
        factura.total = total
        factura.estado = estado
        factura.save()

        messages.success(request, 'Factura actualizada correctamente.')
        return redirect('lista_facturas')


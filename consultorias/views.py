from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from gestion_clientes.models import Cliente
from .models import Consultoria


def lista_consultorias(request):
    # Crear una nueva consultoría
    if request.method == 'POST' and 'crear' in request.POST:
        cliente_id = request.POST.get('cliente')
        descripcion = request.POST.get('descripcion')
        estado = request.POST.get('estado')
        fecha = request.POST.get('fecha')

        cliente = Cliente.objects.filter(id=cliente_id).first()

        if cliente:
            Consultoria.objects.create(
                cliente=cliente,
                descripcion=descripcion,
                estado=estado,
                fecha=fecha
            )
        return redirect('lista_consultorias')

    consultorias = Consultoria.objects.all().order_by('id')
    clientes = Cliente.objects.all()
    consultores = User.objects.all()

    return render(request, 'consultorias/lista_consultorias.html', {
        'consultorias': consultorias,
        'clientes': clientes,
        'consultores': consultores,
    })


def editar_consultoria(request, consultoria_id):
    consultoria = get_object_or_404(Consultoria, id=consultoria_id)

    if request.method == 'POST':
        consultoria.cliente_id = request.POST.get('cliente')
        consultoria.descripcion = request.POST.get('descripcion')
        consultoria.estado = request.POST.get('estado')
        consultoria.fecha = request.POST.get('fecha')
        consultoria.save()
        return redirect('lista_consultorias')

    return redirect('lista_consultorias')


def eliminar_consultoria(request, consultoria_id):
    consultoria = get_object_or_404(Consultoria, id=consultoria_id)
    consultoria.delete()
    return redirect('lista_consultorias')

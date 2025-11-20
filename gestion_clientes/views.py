from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente
from django.contrib.auth.models import User
from django.contrib import messages

def lista_clientes(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        empresa = request.POST.get('empresa')
        correo = request.POST.get('correo')
        telefono = request.POST.get('telefono')
        estado = request.POST.get('estado')
        asignado_id = request.POST.get('asignado')

        asignado = User.objects.filter(id=asignado_id).first() if asignado_id else None

        if Cliente.objects.filter(correo__iexact=correo).exists():
            messages.error(request, "⚠️ Este correo ya está registrado en el sistema.")
            return redirect('lista_clientes')

        Cliente.objects.create(
            asignado=asignado,
            nombre=nombre,
            empresa=empresa,
            correo=correo,
            telefono=telefono,
            estado=estado
        )

        messages.success(request, "✔️ Cliente registrado con éxito.")
        return redirect('lista_clientes')

    clientes = Cliente.objects.all().order_by('id')
    consultores = User.objects.all()
    return render(request, 'gestion_clientes/lista_clientes.html', {
        'clientes': clientes,
        'consultores': consultores
    })


def eliminar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    cliente.delete()
    return redirect('lista_clientes')


def cambiar_estado_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    if request.method == 'POST':
        nuevo_estado = request.POST.get('estado')
        if nuevo_estado in ['activo', 'inactivo', 'pendiente']:
            cliente.estado = nuevo_estado
            cliente.save()
    return redirect('lista_clientes')

def editar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)

    if request.method == 'POST':
        cliente.nombre = request.POST.get('nombre')
        cliente.empresa = request.POST.get('empresa')
        cliente.correo = request.POST.get('correo')
        cliente.telefono = request.POST.get('telefono')
        cliente.estado = request.POST.get('estado')

        asignado_id = request.POST.get('asignado')
        cliente.asignado = User.objects.filter(id=asignado_id).first() if asignado_id else None

        cliente.save()
        return redirect('lista_clientes')


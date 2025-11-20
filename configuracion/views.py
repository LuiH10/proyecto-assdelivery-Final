from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.db import IntegrityError

def configuracion_usuario(request):
    usuario = request.user

    if request.method == 'POST':
        nuevo_nombre = request.POST.get('nombre')
        nuevo_correo = request.POST.get('correo')
        nueva_pass = request.POST.get('password')

        # 🔍 Validar si el username ya existe y NO es el mismo usuario
        if User.objects.filter(username=nuevo_nombre).exclude(id=usuario.id).exists():
            messages.error(request, f"El nombre de usuario '{nuevo_nombre}' ya está en uso.")
            return redirect('configuracion_usuario')

        # 🔍 Validar si el correo ya existe y NO es el mismo usuario (opcional)
        if User.objects.filter(email=nuevo_correo).exclude(id=usuario.id).exists():
            messages.error(request, f"El correo '{nuevo_correo}' ya está en uso.")
            return redirect('configuracion_usuario')

        try:
            # Guardar cambios
            usuario.username = nuevo_nombre
            usuario.email = nuevo_correo

            if nueva_pass:
                usuario.set_password(nueva_pass)

            usuario.save()
            messages.success(request, "Datos actualizados correctamente.")

            return redirect('configuracion_usuario')

        except IntegrityError:
            messages.error(request, "Ocurrió un error: el nombre o correo ya existe.")
            return redirect('configuracion_usuario')

    return render(request, 'configuracion/perfil.html')


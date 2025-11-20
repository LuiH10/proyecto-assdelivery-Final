from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash

@login_required
def configuracion_usuario(request):

    user = request.user  # Usuario actual

    if request.method == 'POST':
        
        nuevo_nombre = request.POST.get('nombre')
        nuevo_correo = request.POST.get('correo')
        nueva_contrasena = request.POST.get('password')

        # ----- Actualizar username -----
        if nuevo_nombre and nuevo_nombre.strip() != "":
            user.username = nuevo_nombre

        # ----- Actualizar email -----
        if nuevo_correo and nuevo_correo.strip() != "":
            user.email = nuevo_correo

        # ----- Actualizar contraseña correctamente -----
        if nueva_contrasena and nueva_contrasena.strip() != "":
            user.set_password(nueva_contrasena) 
            user.save()
            update_session_auth_hash(request, user)  # Mantiene sesión activa
        else:
            user.save()

        messages.success(request, "Cambios guardados correctamente.")
        return redirect('configuracion_usuario')

    return render(request, 'configuracion/perfil.html')

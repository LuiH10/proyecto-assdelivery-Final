from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash


# ===========================
#     PERFIL / CONFIGURACIÓN
# ===========================
@login_required
def configuracion_usuario(request):
    user = request.user

    if request.method == "POST":
        nombre = request.POST.get("nombre")
        correo = request.POST.get("correo")
        password = request.POST.get("password")

        # Validar nombre único
        if User.objects.filter(username=nombre).exclude(id=user.id).exists():
            messages.error(request, "Ese nombre ya está en uso.")
            return redirect("configuracion_usuario")

        # Validar correo único
        if User.objects.filter(email=correo).exclude(id=user.id).exists():
            messages.error(request, "Ese correo ya está en uso.")
            return redirect("configuracion_usuario")

        # Guardar cambios
        user.username = nombre
        user.email = correo

        cambio_password = False
        if password:
            user.set_password(password)
            cambio_password = True

        user.save()

        # 🔥 Evitar que cierre sesión si cambias la contraseña
        if cambio_password:
            update_session_auth_hash(request, user)

        messages.success(request, "Cambios guardados correctamente.")
        return redirect("configuracion_usuario")

    # Mostrar consultores (excepto superusuario y usuario actual)
    consultores = User.objects.exclude(id=request.user.id).exclude(is_superuser=True)

    return render(request, "configuracion/perfil.html", {
        "consultores": consultores
    })


# ===========================
#     ELIMINAR POR ID (OCULTO)
# ===========================
@login_required
def eliminar_consultor(request, user_id):
    usuario = get_object_or_404(User, id=user_id)

    if usuario.is_superuser:
        messages.error(request, "No puedes eliminar al superusuario.")
        return redirect("configuracion_usuario")

    if usuario == request.user:
        messages.error(request, "No puedes eliminarte a ti mismo desde aquí.")
        return redirect("configuracion_usuario")

    usuario.delete()
    messages.success(request, "Consultor eliminado correctamente.")
    return redirect("configuracion_usuario")


# ========================================
#   ELIMINAR CONSULTOR DIRECTO POR CORREO
# ========================================
@login_required
def eliminar_consultor_directo(request):
    if request.method == "POST":
        correo = request.POST.get("correo_consultor")

        # Validar existencia
        try:
            usuario = User.objects.get(email=correo)
        except User.DoesNotExist:
            messages.error(request, "No existe ningún consultor con ese correo.")
            return redirect("configuracion_usuario")

        # Proteger superusuario
        if usuario.is_superuser:
            messages.error(request, "No puedes eliminar al superusuario.")
            return redirect("configuracion_usuario")

        # Evitar autodestrucción
        if usuario == request.user:
            messages.error(request, "No puedes eliminar tu propia cuenta.")
            return redirect("configuracion_usuario")

        usuario.delete()
        messages.success(request, f"Consultor '{usuario.username}' eliminado correctamente.")
        return redirect("configuracion_usuario")

    return redirect("configuracion_usuario")




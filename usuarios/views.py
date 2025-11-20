from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

# -------------------------
#   LOGIN
# -------------------------
def login_view(request):
    if request.method == 'POST':
        identificador = request.POST.get('identificador')
        password = request.POST.get('password')

        user = None

        # 1. Intento con username
        user = authenticate(request, username=identificador, password=password)

        # 2. Intento con email
        if user is None:
            try:
                user_obj = User.objects.get(email=identificador)
                user = authenticate(request, username=user_obj.username, password=password)
            except User.DoesNotExist:
                user = None

        # 3. Resultado
        if user is not None:
            login(request, user)
            return redirect('inicio')
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")

    return render(request, 'usuarios/login.html')

# -------------------------
#   REGISTRO
# -------------------------
def registro_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        correo = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Ese nombre de usuario ya está registrado.")
            return redirect('registro')

        if User.objects.filter(email=correo).exists():
            messages.error(request, "Ese correo ya está registrado.")
            return redirect('registro')

        User.objects.create_user(username=username, email=correo, password=password)
        messages.success(request, "Cuenta creada con éxito. Ahora puedes iniciar sesión.")
        return redirect('login')

    return render(request, 'usuarios/registro.html')

# -------------------------
#   RECUPERAR CONTRASEÑA
# -------------------------
def recuperar_contrasena(request):
    if request.method == 'POST':
        correo = request.POST.get('correo')

        try:
            usuario = User.objects.get(email=correo)
            return redirect('resetear_contrasena', correo=correo)
        except User.DoesNotExist:
            messages.error(request, "El correo no está registrado.")
            return redirect('login')

    return redirect('login')

# -------------------------
#   RESETEAR CONTRASEÑA
# -------------------------
def resetear_contrasena(request, correo):
    usuario = get_object_or_404(User, email=correo)

    if request.method == 'POST':
        nueva = request.POST.get('password')
        usuario.set_password(nueva)
        usuario.save()

        messages.success(request, "Contraseña cambiada con éxito. Inicia sesión.")
        return redirect('login')

    return render(request, 'usuarios/resetear.html', {'correo': correo})

# -------------------------
#   LOGOUT
# -------------------------
def logout_view(request):
    logout(request)
    return redirect('login')

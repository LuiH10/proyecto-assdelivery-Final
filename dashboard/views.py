from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
# Importaciones para el dashboard
from gestion_clientes.models import Cliente  # type: ignore
from consultorias.models import Consultoria  # pyright: ignore
from facturas.models import Factura  # type: ignore
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def inicio_admin(request):
    # Datos reales del panel principal
    datos = {
        'clientes': Cliente.objects.count(),
        'consultorias': Consultoria.objects.count(),
        'facturas_emitidas': Factura.objects.filter(estado='pagada').count(),
        'facturas_pendientes': Factura.objects.filter(estado='pendiente').count(),
        'reportes': 5,
    }
    return render(request, 'dashboard/inicio_admin.html', datos)

# Vista de logout
logout_view = auth_views.LogoutView.as_view(
    next_page='login'
)

# Vista de login (usando Django's LoginView)
login_view = LoginView.as_view(
    template_name='dashboard/login.html',  # Asegúrate de que este template exista
    redirect_authenticated_user=True,  # Redirige si ya logueado
)

# Nueva vista para la raíz: redirige a login si no autenticado, o a inicio_admin si sí
def root_view(request):
    if request.user.is_authenticated:
        return redirect('inicio_admin')  # Redirige al dashboard si logueado
    else:
        return redirect('login')  # Redirige a login si no logueado

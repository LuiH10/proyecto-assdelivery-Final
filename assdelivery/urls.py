# assdelivery/urls.py
from django.contrib import admin
from django.urls import path, include
from usuarios.views import login_view, logout_view
from dashboard.views import inicio_admin

urlpatterns = [
    path('admin/', admin.site.urls),

    # Login y logout
    path('', login_view, name='login'),  # << ESTA ES LA RAÍZ
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    # Panel principal después del login
    path('inicio/', inicio_admin, name='inicio'),

    # Módulos
    path('clientes/', include('gestion_clientes.urls')),
    path('consultorias/', include('consultorias.urls')),
    path('facturas/', include('facturas.urls')),
    path('reportes/', include('reportes.urls')),
    path('configuracion/', include('configuracion.urls')),
    path('usuarios/', include('usuarios.urls')),

]

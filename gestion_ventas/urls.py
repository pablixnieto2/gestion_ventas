# gestion_ventas/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/', include('clientes.urls')),
    path('ventas/', include('ventas.urls')),
    path('productos/', include('productos.urls')),
    path('pedidos/', include('pedidos.urls')),
    path('sesiones_fotos/', include('sesiones_fotos.urls')),
]

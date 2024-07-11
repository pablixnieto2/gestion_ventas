from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/', include('clientes.urls')),
    path('productos/', include('productos.urls')),
    path('pagos/', include('pagos.urls')),
    path('pedidos/', include('pedidos.urls')),
    path('sesiones_fotos/', include('sesiones_fotos.urls')),
    path('ventas/', include('ventas.urls')),
    path('', include('home.urls')),  # Assuming you have a home app for the landing page
]

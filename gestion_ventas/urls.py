from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ventas/', include('ventas.urls')),
    path('clientes/', include('clientes.urls')),
    path('productos/', include('productos.urls')),
    path('pagos/', include('pagos.urls')),
    path('sesiones-fotos/', include('sesiones_fotos.urls')),
    path('pedidos/', include('pedidos.urls')),
    path('api-auth/', include('rest_framework.urls')),
]

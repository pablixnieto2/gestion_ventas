from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from ventas import views as ventas_views
from clientes import views as clientes_views
from productos import views as productos_views
from pagos import views as pagos_views
from sesiones_fotos import views as sesiones_fotos_views
from pedidos import views as pedidos_views

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'ventas', ventas_views.VentaViewSet)
router.register(r'clientes', clientes_views.ClienteViewSet)
router.register(r'productos', productos_views.ProductoViewSet)
router.register(r'pagos', pagos_views.PagoViewSet)
router.register(r'sesiones-fotos', sesiones_fotos_views.SesionFotoViewSet)
router.register(r'pedidos', pedidos_views.PedidoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ventas/', include('ventas.urls')),
    path('clientes/', include('clientes.urls')),
    path('productos/', include('productos.urls')),
    path('pagos/', include('pagos.urls')),
    path('sesiones-fotos/', include('sesiones_fotos.urls')),
    path('pedidos/', include('pedidos.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),  # API routes
    # path('docs/', include_docs_urls(title='My API title')),  # API documentation
]

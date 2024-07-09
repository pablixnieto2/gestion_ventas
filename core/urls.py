from django.urls import path
from . import views  # Asegúrate de importar views correctamente
from .views import (
    ClienteListView, ClienteDetailView, ClienteCreateView, ClienteUpdateView, ClienteDeleteView,
    ProductoListView, ProductoDetailView, ProductoCreateView, ProductoUpdateView, ProductoDeleteView,
    VentaListView, VentaDetailView, VentaCreateView, VentaUpdateView, VentaDeleteView,
    PagoListView, PagoDetailView, PagoCreateView, PagoUpdateView, PagoDeleteView
)

urlpatterns = [
    path('', views.home, name='home'),

    path('clientes/', ClienteListView.as_view(), name='cliente-list'),
    path('clientes/<int:pk>/', ClienteDetailView.as_view(), name='cliente-detail'),
    path('clientes/create/', ClienteCreateView.as_view(), name='cliente-create'),
    path('clientes/<int:pk>/update/', ClienteUpdateView.as_view(), name='cliente-update'),
    path('clientes/<int:pk>/delete/', ClienteDeleteView.as_view(), name='cliente-delete'),

    path('productos/', ProductoListView.as_view(), name='producto-list'),
    path('productos/<int:pk>/', ProductoDetailView.as_view(), name='producto-detail'),
    path('productos/create/', ProductoCreateView.as_view(), name='producto-create'),
    path('productos/<int:pk>/update/', ProductoUpdateView.as_view(), name='producto-update'),
    path('productos/<int:pk>/delete/', ProductoDeleteView.as_view(), name='producto-delete'),

    path('ventas/', VentaListView.as_view(), name='venta-list'),
    path('ventas/<int:pk>/', VentaDetailView.as_view(), name='venta-detail'),
    path('ventas/create/', VentaCreateView.as_view(), name='venta-create'),
    path('ventas/<int:pk>/update/', VentaUpdateView.as_view(), name='venta-update'),
    path('ventas/<int:pk>/delete/', VentaDeleteView.as_view(), name='venta-delete'),

    path('pagos/', PagoListView.as_view(), name='pago-list'),
    path('pagos/<int:pk>/', PagoDetailView.as_view(), name='pago-detail'),
    path('pagos/create/', PagoCreateView.as_view(), name='pago-create'),
    path('pagos/<int:pk>/update/', PagoUpdateView.as_view(), name='pago-update'),
    path('pagos/<int:pk>/delete/', PagoDeleteView.as_view(), name='pago-delete'),
]

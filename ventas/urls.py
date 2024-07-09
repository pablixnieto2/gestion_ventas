from django.urls import path
from . import views

urlpatterns = [
    path('crear_venta_producto/', views.crear_venta_producto, name='crear_venta_producto'),
    path('crear_venta_alquiler/', views.crear_venta_alquiler, name='crear_venta_alquiler'),
    path('producto_venta_list/', views.producto_venta_list, name='producto_venta_list'),
    path('producto_alquiler_list/', views.producto_alquiler_list, name='producto_alquiler_list'),
    path('producto_venta_detail/<int:id>/', views.producto_venta_detail, name='producto_venta_detail'),
    path('producto_alquiler_detail/<int:id>/', views.producto_alquiler_detail, name='producto_alquiler_detail'),
]

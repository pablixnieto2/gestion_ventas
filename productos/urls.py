from django.urls import path
from . import views

urlpatterns = [
    path('', views.producto_list, name='producto_list'),
    path('venta/', views.producto_venta_list, name='producto_venta_list'),
    path('alquiler/', views.producto_alquiler_list, name='producto_alquiler_list'),
    path('venta/<int:id>/', views.producto_venta_detail, name='producto_venta_detail'),
    path('alquiler/<int:id>/', views.producto_alquiler_detail, name='producto_alquiler_detail'),
    path('crear_venta/', views.crear_producto_venta, name='crear_producto_venta'),
    path('crear_alquiler/', views.crear_producto_alquiler, name='crear_producto_alquiler'),
]

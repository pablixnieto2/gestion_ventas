from django.urls import path
from . import views

urlpatterns = [
    path('venta/', views.producto_venta_list, name='producto_venta_list'),
    path('alquiler/', views.producto_alquiler_list, name='producto_alquiler_list'),
    path('venta/<int:id>/', views.producto_venta_detail, name='producto_venta_detail'),
    path('alquiler/<int:id>/', views.producto_alquiler_detail, name='producto_alquiler_detail'),
]

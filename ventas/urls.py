# ventas/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.venta_list, name='venta_list'),
    path('<int:id>/', views.venta_detail, name='venta_detail'),
    path('crear_producto/', views.crear_venta_producto, name='crear_venta_producto'),
    path('crear_alquiler/', views.crear_venta_alquiler, name='crear_venta_alquiler'),
]

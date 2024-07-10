from django.urls import path
from . import views

urlpatterns = [
    path('', views.cliente_list, name='cliente_list'),
    path('<int:id>/', views.cliente_detail, name='cliente_detail'),
    path('crear/', views.crear_cliente, name='crear_cliente'),
]

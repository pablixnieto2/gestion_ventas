from django.urls import path
from . import views

urlpatterns = [
    path('', views.pedido_list, name='pedido_list'),
    path('<int:id>/', views.pedido_detail, name='pedido_detail'),
    path('crear/', views.crear_pedido, name='crear_pedido'),
]

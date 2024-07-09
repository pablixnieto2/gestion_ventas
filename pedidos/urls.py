from django.urls import path
from . import views

urlpatterns = [
    # Define tus URL patterns aquí
    path('', views.pedido_list, name='pedido_list'),
    path('<int:id>/', views.pedido_detail, name='pedido_detail'),
]

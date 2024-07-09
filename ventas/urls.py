from django.urls import path
from . import views

urlpatterns = [
    # Define tus URL patterns aquí
    path('', views.venta_list, name='venta_list'),
    path('<int:id>/', views.venta_detail, name='venta_detail'),
]

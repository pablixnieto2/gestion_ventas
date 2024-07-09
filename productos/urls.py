from django.urls import path
from . import views

urlpatterns = [
    # Define tus URL patterns aquí
    path('', views.producto_list, name='producto_list'),
    path('<int:id>/', views.producto_detail, name='producto_detail'),
]

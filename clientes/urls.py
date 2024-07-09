from django.urls import path
from . import views

urlpatterns = [
    # Define tus URL patterns aquí
    path('', views.cliente_list, name='cliente_list'),
    path('<int:id>/', views.cliente_detail, name='cliente_detail'),
]

from django.urls import path
from . import views

urlpatterns = [
    # Define tus URL patterns aquí
    path('', views.pago_list, name='pago_list'),
    path('<int:id>/', views.pago_detail, name='pago_detail'),
]

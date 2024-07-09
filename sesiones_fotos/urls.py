from django.urls import path
from . import views

urlpatterns = [
    # Define tus URL patterns aquí
    path('', views.sesion_foto_list, name='sesion_foto_list'),
    path('<int:id>/', views.sesion_foto_detail, name='sesion_foto_detail'),
]

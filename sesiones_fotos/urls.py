from django.urls import path
from . import views

urlpatterns = [
    path('', views.sesion_foto_list, name='sesion_foto_list'),
    path('<int:id>/', views.sesion_foto_detail, name='sesion_foto_detail'),
    path('crear/', views.crear_sesion_foto, name='crear_sesion_foto'),
]

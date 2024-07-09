#!/bin/bash

for app in ventas clientes productos pagos sesiones_fotos pedidos; do
    cd $app
    
    echo "from django.contrib import admin
from .models import *  # Importar todos los modelos

# Registrar todos los modelos automáticamente
for model in models.__all__:
    admin.site.register(getattr(models, model))" > admin.py
    
    echo "from django.apps import AppConfig

class $(echo $app | sed -r 's/(^|-)(\w)/\U\2/g')Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = '$app'" > apps.py
    
    echo "from django.test import TestCase

# Create your tests here." > tests.py
    
    echo "from django.shortcuts import render

# Create your views here." > views.py
    
    echo "from django.urls import path
from . import views

urlpatterns = [
    # Define your URL patterns here
]" > urls.py
    
    cd ..
done


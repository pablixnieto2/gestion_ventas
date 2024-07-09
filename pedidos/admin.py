from django.contrib import admin
from .models import *  # Importar todos los modelos

# Registrar todos los modelos automáticamente
for model in models.__all__:
    admin.site.register(getattr(models, model))

# sesiones_fotos/forms.py
from django import forms
from .models import SesionFotos

class SesionFotoForm(forms.ModelForm):
    class Meta:
        model = SesionFotos
        fields = '__all__'

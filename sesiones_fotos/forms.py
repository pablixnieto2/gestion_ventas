# sesiones_fotos/forms.py
from django import forms
from .models import SesionFoto

class SesionFotoForm(forms.ModelForm):
    class Meta:
        model = SesionFoto
        fields = '__all__'

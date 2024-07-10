from django import forms
from .models import ProductoVenta, ProductoAlquiler

class ProductoVentaForm(forms.ModelForm):
    class Meta:
        model = ProductoVenta
        fields = '__all__'

class ProductoAlquilerForm(forms.ModelForm):
    class Meta:
        model = ProductoAlquiler
        fields = '__all__'

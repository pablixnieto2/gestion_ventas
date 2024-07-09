from django import forms
from .models import Cliente, Producto, Venta, VentaProducto, Pago
from bootstrap_datepicker_plus.widgets import DatePickerInput

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'fecha_fiesta', 
            'nombre', 
            'apellido', 
            'prefijo', 
            'telefono', 
            'email', 
            'ubicacion', 
            'estado', 
            'como_nos_conocio', 
            'comentarios'
        ]
        widgets = {
            'fecha_fiesta': DatePickerInput(),  # Date picker para la fecha de la fiesta
            'prefijo': forms.Select(choices=[
                ('+34', '+34'), 
                ('+1', '+1'), 
                ('+44', '+44')
            ]),  # Prefijos predefinidos
        }


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            'nombre', 
            'categoria', 
            'color', 
            'talla', 
            'pvp', 
            'imagen', 
            'estado', 
            'tienda', 
            'cantidad_madrid', 
            'cantidad_barcelona', 
            'cantidad_valencia', 
            'cantidad_videollamada'
        ]

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = [
            'tienda', 
            'envio_entrega', 
            'tipo', 
            'cliente', 
            'fecha_entrega', 
            'fecha_devolucion'
        ]
        widgets = {
            'fecha_entrega': DatePickerInput(),  # Date picker para la fecha de entrega
            'fecha_devolucion': DatePickerInput(),  # Date picker para la fecha de devolución
            'tienda': forms.Select(choices=[
                ('Madrid', 'Madrid'), 
                ('Barcelona', 'Barcelona'),
                ('Valencia', 'Valencia'),
                ('Videollamada', 'Videollamada')
            ]),
            'envio_entrega': forms.Select(choices=[
                ('Envio', 'Envio'), 
                ('Entrega en tienda', 'Entrega en tienda')
            ]),
            'tipo': forms.Select(choices=[
                ('Alquiler', 'Alquiler'), 
                ('Venta', 'Venta')
            ]),
        }

class VentaProductoForm(forms.ModelForm):
    class Meta:
        model = VentaProducto
        fields = ['producto', 'cantidad']

class PagoForm(forms.ModelForm):
    class Meta:
        model = Pago
        fields = ['venta', 'metodo_pago', 'importe']
        widgets = {
            'venta': forms.Select(),
            'metodo_pago': forms.Select(),
            'importe': forms.NumberInput(attrs={'class': 'form-control'}),
        }

# Inline formset para Venta y VentaProducto
VentaProductoFormSet = forms.inlineformset_factory(Venta, VentaProducto, form=VentaProductoForm, extra=1)

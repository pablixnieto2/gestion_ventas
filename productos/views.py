from django.shortcuts import render, get_object_or_404
from .models import ProductoVenta, ProductoAlquiler

def producto_venta_list(request):
    productos_venta = ProductoVenta.objects.all()
    return render(request, 'productos/producto_venta_list.html', {'productos_venta': productos_venta})

def producto_alquiler_list(request):
    productos_alquiler = ProductoAlquiler.objects.all()
    return render(request, 'productos/producto_alquiler_list.html', {'productos_alquiler': productos_alquiler})

def producto_venta_detail(request, id):
    producto_venta = get_object_or_404(ProductoVenta, id=id)
    return render(request, 'productos/producto_venta_detail.html', {'producto_venta': producto_venta})

def producto_alquiler_detail(request, id):
    producto_alquiler = get_object_or_404(ProductoAlquiler, id=id)
    return render(request, 'productos/producto_alquiler_detail.html', {'producto_alquiler': producto_alquiler})

# ventas/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.core.exceptions import ValidationError
from .models import Venta
from .forms import VentaForm
from productos.models import ProductoVenta, ProductoAlquiler, ReservaAlquiler

def venta_list(request):
    ventas = Venta.objects.all()
    return render(request, 'ventas/venta_list.html', {'ventas': ventas})

def venta_detail(request, id):
    venta = get_object_or_404(Venta, id=id)
    return render(request, 'ventas/venta_detail.html', {'venta': venta})

def crear_venta_producto(request):
    if request.method == 'POST':
        form = VentaForm(request.POST, request.FILES)
        if form.is_valid():
            venta = form.save(commit=False)
            producto_id = request.POST.get('producto_id')
            producto = get_object_or_404(ProductoVenta, id=producto_id)
            venta.save()
            venta.productos_venta.add(producto)
            return redirect('venta_detail', id=venta.id)
    else:
        form = VentaForm()
    return render(request, 'ventas/crear_venta_producto.html', {'form': form})

def crear_venta_alquiler(request):
    if request.method == 'POST':
        form = VentaForm(request.POST, request.FILES)
        if form.is_valid():
            venta = form.save(commit=False)
            producto_id = request.POST.get('producto_id')
            producto = get_object_or_404(ProductoAlquiler, id=producto_id)
            start_date = request.POST.get('fecha_entrega')
            end_date = request.POST.get('fecha_devolucion')
            reserva = ReservaAlquiler(producto=producto, start_date=start_date, end_date=end_date)
            try:
                reserva.clean()
                reserva.save()
                venta.save()
                venta.productos_alquiler.add(producto)
                return redirect('venta_detail', id=venta.id)
            except ValidationError as e:
                return render(request, 'error.html', {'error': e.message})
    else:
        form = VentaForm()
    return render(request, 'ventas/crear_venta_alquiler.html', {'form': form})

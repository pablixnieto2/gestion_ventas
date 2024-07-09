from django.shortcuts import render, get_object_or_404
from django.core.exceptions import ValidationError
from .models import Venta
from productos.models import ProductoVenta, ProductoAlquiler, ReservaAlquiler

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

def crear_venta_alquiler(request):
    if request.method == 'POST':
        producto_id = request.POST.get('producto_id')
        producto = get_object_or_404(ProductoAlquiler, id=producto_id)
        start_date = request.POST.get('fecha_entrega')
        end_date = request.POST.get('fecha_devolucion')

        reserva = ReservaAlquiler(producto=producto, start_date=start_date, end_date=end_date)

        try:
            reserva.clean()
            reserva.save()
            venta = Venta.objects.create(
                id_ventas=request.POST.get('id_ventas'),
                created_by=request.POST.get('created_by'),
                tienda=request.POST.get('tienda'),
                tipo='Alquiler',
                id_clientes=request.POST.get('id_clientes'),
                fecha_entrega=start_date,
                fecha_devolucion=end_date,
                total_a_pagar=request.POST.get('total_a_pagar'),
                total_pagado=request.POST.get('total_pagado'),
                pendiente_de_pago=request.POST.get('pendiente_de_pago'),
                estado_pago=request.POST.get('estado_pago'),
                comentarios=request.POST.get('comentarios'),
            )
            venta.productos_alquiler.add(producto)
            venta.save()
            return render(request, 'ventas/venta_detail.html', {'venta': venta})
        except ValidationError as e:
            return render(request, 'error.html', {'error': e.message})

    return render(request, 'ventas/crear_venta_alquiler.html')

def crear_venta_producto(request):
    if request.method == 'POST':
        producto_id = request.POST.get('producto_id')
        producto = get_object_or_404(ProductoVenta, id=producto_id)

        try:
            producto.clean()
            venta = Venta.objects.create(
                id_ventas=request.POST.get('id_ventas'),
                created_by=request.POST.get('created_by'),
                tienda=request.POST.get('tienda'),
                tipo='Venta',
                id_clientes=request.POST.get('id_clientes'),
                fecha_entrega=request.POST.get('fecha_entrega'),
                total_a_pagar=request.POST.get('total_a_pagar'),
                total_pagado=request.POST.get('total_pagado'),
                pendiente_de_pago=request.POST.get('pendiente_de_pago'),
                estado_pago=request.POST.get('estado_pago'),
                comentarios=request.POST.get('comentarios'),
            )
            venta.productos_venta.add(producto)
            venta.save()
            return render(request, 'ventas/venta_detail.html', {'venta': venta})
        except ValidationError as e:
            return render(request, 'error.html', {'error': e.message})

    return render(request, 'ventas/crear_venta_producto.html')

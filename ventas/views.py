from django.shortcuts import render, get_object_or_404
from .models import Venta

def venta_list(request):
    ventas = Venta.objects.all()
    return render(request, 'ventas/venta_list.html', {'ventas': ventas})

def venta_detail(request, id):
    venta = get_object_or_404(Venta, id=id)
    return render(request, 'ventas/venta_detail.html', {'venta': venta})

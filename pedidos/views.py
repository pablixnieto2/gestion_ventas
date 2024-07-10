from django.shortcuts import render, get_object_or_404
from .models import Pedido

def pedido_list(request):
    pedidos = Pedido.objects.all()
    return render(request, 'pedidos/pedido_list.html', {'pedidos': pedidos})

def pedido_detail(request, id):
    pedido = get_object_or_404(Pedido, id=id)
    return render(request, 'pedidos/pedido_detail.html', {'pedido': pedido})

def crear_pedido(request):
    if request.method == 'POST':
        # Lógica para crear pedido
        pass
    return render(request, 'pedidos/crear_pedido.html')

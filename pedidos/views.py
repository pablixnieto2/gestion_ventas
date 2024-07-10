# pedidos/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Pedido
from .forms import PedidoForm

def pedido_list(request):
    pedidos = Pedido.objects.all()
    return render(request, 'pedidos/pedido_list.html', {'pedidos': pedidos})

def pedido_detail(request, id):
    pedido = get_object_or_404(Pedido, id=id)
    return render(request, 'pedidos/pedido_detail.html', {'pedido': pedido})

def crear_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pedido_list')
    else:
        form = PedidoForm()
    return render(request, 'pedidos/crear_pedido.html', {'form': form})

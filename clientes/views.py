from django.shortcuts import render, get_object_or_404, redirect
from .models import Cliente
from .forms import ClienteForm

def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/listar_cliente.html', {'clientes': clientes})

def cliente_detail(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    return render(request, 'clientes/cliente_detail.html', {'cliente': cliente})

def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cliente_list')
    else:
        form = ClienteForm()
    return render(request, 'clientes/crear_cliente.html', {'form': form})

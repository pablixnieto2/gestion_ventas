from django.shortcuts import render, get_object_or_404
from .models import Cliente

def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/cliente_list.html', {'clientes': clientes})

def cliente_detail(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    return render(request, 'clientes/cliente_detail.html', {'cliente': cliente})

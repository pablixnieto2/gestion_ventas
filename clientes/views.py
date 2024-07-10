from django.shortcuts import render, get_object_or_404, redirect
from .models import Cliente

def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/cliente_list.html', {'clientes': clientes})

def cliente_detail(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    return render(request, 'clientes/cliente_detail.html', {'cliente': cliente})

def crear_cliente(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        fecha_fiesta = request.POST.get('fecha_fiesta')
        Cliente.objects.create(nombre=nombre, apellido=apellido, email=email, telefono=telefono, fecha_fiesta=fecha_fiesta)
        return redirect('cliente_list')
    return render(request, 'clientes/crear_cliente.html')

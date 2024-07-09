from django.shortcuts import render, get_object_or_404
from .models import Pago

def pago_list(request):
    pagos = Pago.objects.all()
    return render(request, 'pagos/pago_list.html', {'pagos': pagos})

def pago_detail(request, id):
    pago = get_object_or_404(Pago, id=id)
    return render(request, 'pagos/pago_detail.html', {'pago': pago})

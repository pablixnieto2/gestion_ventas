# sesiones_fotos/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import SesionFotos
from .forms import SesionFotoForm

def sesion_foto_list(request):
    sesiones_fotos = SesionFoto.objects.all()
    return render(request, 'sesiones_fotos/sesion_foto_list.html', {'sesiones_fotos': sesiones_fotos})

def sesion_foto_detail(request, id):
    sesion_foto = get_object_or_404(SesionFoto, id=id)
    return render(request, 'sesiones_fotos/sesion_foto_detail.html', {'sesion_foto': sesion_foto})

def crear_sesion_foto(request):
    if request.method == 'POST':
        form = SesionFotoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sesion_foto_list')
    else:
        form = SesionFotoForm()
    return render(request, 'sesiones_fotos/crear_sesion_foto.html', {'form': form})


def index(request):
    sesiones = SesionFotos.objects.all()
    return render(request, 'sesiones_fotos/index.html', {'sesiones': sesiones})

from django.shortcuts import render, get_object_or_404
from .models import SesionFoto

def sesion_foto_list(request):
    sesiones = SesionFoto.objects.all()
    return render(request, 'sesiones_fotos/sesion_foto_list.html', {'sesiones': sesiones})

def sesion_foto_detail(request, id):
    sesion = get_object_or_404(SesionFoto, id=id)
    return render(request, 'sesiones_fotos/sesion_foto_detail.html', {'sesion': sesion})

def crear_sesion_foto(request):
    if request.method == 'POST':
        # Lógica para crear sesión de fotos
        pass
    return render(request, 'sesiones_fotos/crear_sesion_foto.html')

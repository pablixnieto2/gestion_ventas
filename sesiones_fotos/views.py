from django.shortcuts import render, get_object_or_404
from .models import SesionFoto

def sesion_foto_list(request):
    sesiones_fotos = SesionFoto.objects.all()
    return render(request, 'sesiones_fotos/sesion_foto_list.html', {'sesiones_fotos': sesiones_fotos})

def sesion_foto_detail(request, id):
    sesion_foto = get_object_or_404(SesionFoto, id=id)
    return render(request, 'sesiones_fotos/sesion_foto_detail.html', {'sesion_foto': sesion_foto})

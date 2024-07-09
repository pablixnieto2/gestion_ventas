from django.db import models
from simple_history.models import HistoricalRecords
from ventas.models import Venta

class SesionFoto(models.Model):
    id_sesion = models.CharField(max_length=6, unique=True)
    id_ventas = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name='sesiones_fotos')
    fecha_sesion = models.DateTimeField()
    lugar_sesion = models.CharField(max_length=255)
    nombre_fotografo = models.CharField(max_length=255)
    comentarios = models.TextField(null=True, blank=True)
    fotos_entregadas = models.BooleanField(default=False)
    history = HistoricalRecords()

    def __str__(self):
        return f"Sesión {self.id_sesion} - {self.nombre_fotografo}"

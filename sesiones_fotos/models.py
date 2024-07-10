from django.db import models
from simple_history.models import HistoricalRecords
from ventas.models import Venta

class SesionFotos(models.Model):
    id_sesion = models.CharField(max_length=6, unique=True)
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name='sesiones_fotos')
    fecha_sesion = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    ubicacion = models.CharField(max_length=100)
    fotografo = models.CharField(max_length=100)
    comentarios = models.TextField(null=True, blank=True)
    estado = models.CharField(max_length=50, choices=[('Pendiente', 'Pendiente'), ('Completada', 'Completada'), ('Cancelada', 'Cancelada')])
    history = HistoricalRecords()

    def __str__(self):
        return f"Sesión de Fotos {self.id_sesion} - {self.venta.id_ventas} - {self.fecha_sesion}"

    @property
    def duracion(self):
        from datetime import datetime, date
        return (datetime.combine(date.min, self.hora_fin) - datetime.combine(date.min, self.hora_inicio)).seconds / 3600

    @property
    def estado_display(self):
        return self.estado

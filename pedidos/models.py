from django.db import models
from simple_history.models import HistoricalRecords
from ventas.models import Venta
import uuid

class Pedido(models.Model):
    id_pedido = models.CharField(max_length=6, unique=True, default=uuid.uuid4().hex[:6].upper())
    id_ventas = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name='pedidos')
    proveedor = models.CharField(max_length=255)
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    fecha_entrega = models.DateField()
    estado = models.CharField(max_length=50, choices=[('Pendiente', 'Pendiente'), ('En Proceso', 'En Proceso'), ('Completado', 'Completado'), ('Cancelado', 'Cancelado')])
    comentarios = models.TextField(null=True, blank=True)
    history = HistoricalRecords()

    def __str__(self):
        return f"Pedido {self.id_pedido} - {self.proveedor}"

    @property
    def estado_display(self):
        if self.estado == 'Pendiente':
            return "Pendiente"
        elif self.estado == 'En Proceso':
            return "En Proceso"
        elif self.estado == 'Completado':
            return "Completado"
        else:
            return "Cancelado"

    @property
    def fecha_estimada_entrega(self):
        return self.fecha_entrega

from django.db import models
from simple_history.models import HistoricalRecords
from ventas.models import Venta

class Pedido(models.Model):
    id_pedido = models.CharField(max_length=6, unique=True)
    id_ventas = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name='pedidos')
    proveedor = models.CharField(max_length=255)
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    fecha_entrega = models.DateField()
    estado = models.CharField(max_length=50, choices=[('Pendiente', 'Pendiente'), ('En Proceso', 'En Proceso'), ('Completado', 'Completado')])
    comentarios = models.TextField(null=True, blank=True)
    history = HistoricalRecords()

    def __str__(self):
        return f"Pedido {self.id_pedido} - {self.proveedor}"

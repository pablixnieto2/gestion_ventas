from django.db import models
from simple_history.models import HistoricalRecords
from ventas.models import Venta

class Pago(models.Model):
    id_pago = models.CharField(max_length=6, unique=True)
    id_ventas = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name='pagos')
    created_by = models.EmailField()
    creation_date = models.DateTimeField(auto_now_add=True)
    tienda = models.CharField(max_length=20, choices=[('Madrid', 'Madrid'), ('Barcelona', 'Barcelona'), ('Valencia', 'Valencia'), ('Videollamada', 'Videollamada')])
    metodo_de_pago = models.CharField(max_length=20, choices=[('Efectivo', 'Efectivo'), ('Tarjeta', 'Tarjeta'), ('BBVA', 'BBVA'), ('SumUp', 'SumUp'), ('Bizum', 'Bizum'), ('Transferencia', 'Transferencia'), ('Paypal', 'Paypal'), ('Web', 'Web')])
    importe = models.DecimalField(max_digits=10, decimal_places=2)
    n_f_simplificada = models.CharField(max_length=255, null=True, blank=True)
    productos_comprados = models.TextField(null=True, blank=True)
    detalles_del_ticket = models.TextField(null=True, blank=True)
    lista_de_productos = models.TextField(null=True, blank=True)
    duplicados = models.BooleanField(default=False)
    history = HistoricalRecords()

    def __str__(self):
        return f"Pago {self.id_pago} - {self.tienda}"

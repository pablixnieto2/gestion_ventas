from django.db import models
from simple_history.models import HistoricalRecords

class Producto(models.Model):
    id_productos = models.CharField(max_length=6, unique=True)
    label_precio = models.CharField(max_length=255)
    almacen_m = models.IntegerField(default=0)
    madrid = models.IntegerField(default=0)
    barcelona = models.IntegerField(default=0)
    tienda = models.CharField(max_length=20, choices=[('Madrid', 'Madrid'), ('Barcelona', 'Barcelona'), ('Valencia', 'Valencia'), ('Videollamada', 'Videollamada')])
    categoria = models.CharField(max_length=50, choices=[('Vestido', 'Vestido'), ('Vestido Corto', 'Vestido Corto'), ('Accesorios', 'Accesorios'), ('Complementos', 'Complementos'), ('Envio', 'Envio'), ('Invitaciones', 'Invitaciones'), ('Paquete Fotos', 'Paquete Fotos'), ('Recuerdos', 'Recuerdos'), ('Otros', 'Otros')])
    nombre = models.CharField(max_length=255)
    color = models.CharField(max_length=50)
    talla = models.CharField(max_length=50)
    pvp = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='productos/', null=True, blank=True)
    estado = models.CharField(max_length=50, choices=[('Activo', 'Activo'), ('Baja', 'Baja')])
    nombres = models.CharField(max_length=255)
    reservados = models.IntegerField(default=0)
    disponibles = models.IntegerField(default=0)
    history = HistoricalRecords()

    def __str__(self):
        return f"{self.nombre} - {self.tienda}"

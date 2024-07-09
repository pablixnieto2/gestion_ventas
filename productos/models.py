from django.db import models
from django.core.exceptions import ValidationError
from simple_history.models import HistoricalRecords

class ProductoVenta(models.Model):
    id_producto = models.CharField(max_length=6, unique=True)
    nombre = models.CharField(max_length=255)
    categoria = models.CharField(max_length=50, choices=[('Vestido', 'Vestido'), ('Accesorios', 'Accesorios'), ('Complementos', 'Complementos'), ('Otros', 'Otros')])
    color = models.CharField(max_length=50)
    talla = models.CharField(max_length=50)
    pvp = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='productos/venta/', null=True, blank=True)
    estado = models.CharField(max_length=50, choices=[('Activo', 'Activo'), ('Baja', 'Baja')])
    stock = models.IntegerField(default=0)
    history = HistoricalRecords()

    def clean(self):
        if self.stock <= 0:
            raise ValidationError('Este producto no tiene stock disponible para la venta.')

    def __str__(self):
        return f"{self.nombre} - {self.categoria}"

class ProductoAlquiler(models.Model):
    id_producto = models.CharField(max_length=6, unique=True)
    nombre = models.CharField(maxlength=255)
    categoria = models.CharField(maxlength=50, choices=[('Vestido', 'Vestido'), ('Accesorios', 'Accesorios'), ('Complementos', 'Complementos'), ('Otros', 'Otros')])
    color = models.CharField(maxlength=50)
    talla = models.CharField(maxlength=50)
    precio_alquiler = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='productos/alquiler/', null=True, blank=True)
    estado = models.CharField(maxlength=50, choices=[('Activo', 'Activo'), ('Baja', 'Baja')])
    stock = models.IntegerField(default=0)
    history = HistoricalRecords()

    def is_available(self, start_date, end_date):
        conflicts = self.reservaalquiler_set.filter(
            start_date__lt=end_date, end_date__gt=start_date
        )
        return not conflicts.exists()

    def __str__(self):
        return f"{self.nombre} - {self.categoria}"

class ReservaAlquiler(models.Model):
    producto = models.ForeignKey(ProductoAlquiler, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def clean(self):
        if not self.producto.is_available(self.start_date, self.end_date):
            raise ValidationError('El producto ya está alquilado para estas fechas.')

    def __str__(self):
        return f"{self.producto.nombre} reservado desde {self.start_date} hasta {self.end_date}"

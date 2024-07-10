from django.db import models
from simple_history.models import HistoricalRecords

class Cliente(models.Model):
    id_clientes = models.CharField(max_length=6, unique=True)
    created_by = models.EmailField()
    creation_date = models.DateTimeField(auto_now_add=True)
    fecha_fiesta = models.DateField(null=True, blank=True)  # Permitir valores nulos
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    prefijo = models.CharField(max_length=3)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()
    ubicacion = models.CharField(max_length=20, choices=[('Madrid', 'Madrid'), ('Valencia', 'Valencia'), ('Barcelona', 'Barcelona'), ('Videollamada', 'Videollamada')])
    estado = models.CharField(max_length=50, choices=[('sin cita', 'sin cita'), ('con cita', 'con cita'), ('perdido', 'perdido'), ('eliminar cliente duplicado', 'eliminar cliente duplicado')])
    como_nos_conocio = models.CharField(max_length=20, choices=[('Google', 'Google'), ('Google maps', 'Google maps'), ('Instagram', 'Instagram'), ('Facebook', 'Facebook'), ('Recomendación', 'Recomendación'), ('Milanuncios', 'Milanuncios'), ('Web', 'Web'), ('Otro', 'Otro')])
    label_clientes = models.CharField(max_length=255)
    whatsapp = models.CharField(max_length=255)
    comentarios = models.TextField(null=True, blank=True)
    razon_perdida = models.CharField(max_length=255, null=True, blank=True)
    codigo_postal = models.CharField(max_length=10)
    vendedora = models.CharField(max_length=100)
    estado_cliente = models.CharField(max_length=50, choices=[('ya compró', 'ya compró'), ('perdido', 'perdido')])
    duplicados = models.BooleanField(default=False)
    ventas_relacionadas = models.TextField()
    color = models.CharField(max_length=50)
    telefono2 = models.CharField(max_length=15)
    label_clientes2 = models.CharField(max_length=255)
    related_sesiones_fotos = models.TextField()
    end_time = models.DateTimeField(null=True, blank=True)
    start_time = models.DateTimeField(null=True, blank=True)
    history = HistoricalRecords()

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.telefono}"

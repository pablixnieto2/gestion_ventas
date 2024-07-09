from django.db import models
from simple_history.models import HistoricalRecords
from clientes.models import Cliente
from productos.models import ProductoVenta, ProductoAlquiler

class Venta(models.Model):
    id_ventas = models.CharField(max_length=6, unique=True)
    created_by = models.EmailField()
    creation_date = models.DateTimeField(auto_now_add=True)
    change_timestamp = models.DateTimeField(auto_now=True)
    tienda = models.CharField(max_length=20, choices=[('Madrid', 'Madrid'), ('Barcelona', 'Barcelona'), ('Valencia', 'Valencia'), ('Videollamada', 'Videollamada')])
    envio_entrega = models.BooleanField(default=False)
    estado_entrega = models.CharField(max_length=50, choices=[('Por Entregar o Enviar', 'Por Entregar o Enviar'), ('Entregado o Enviado', 'Entregado o Enviado'), ('Vestido Devuelto', 'Vestido Devuelto')])
    tipo = models.CharField(max_length=20, choices=[('Alquiler', 'Alquiler'), ('Venta', 'Venta')])
    id_clientes = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    productos_venta = models.ManyToManyField(ProductoVenta, blank=True)
    productos_alquiler = models.ManyToManyField(ProductoAlquiler, blank=True)
    fecha_entrega = models.DateField()
    fecha_devolucion = models.DateField(null=True, blank=True)
    amount_deposito = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    estado_deposito = models.CharField(max_length=50, choices=[('Pendiente de Entrega', 'Pendiente de Entrega'), ('Entregado por el Cliente', 'Entregado por el Cliente'), ('Devuelto al Cliente', 'Devuelto al Cliente')], null=True, blank=True)
    firma = models.ImageField(upload_to='firmas/', null=True, blank=True)
    direccion = models.TextField(null=True, blank=True)
    precio_envio = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    total_a_pagar = models.DecimalField(max_digits=10, decimal_places=2)
    total_pagado = models.DecimalField(max_digits=10, decimal_places=2)
    pendiente_de_pago = models.DecimalField(max_digits=10, decimal_places=2)
    estado_pago = models.CharField(max_length=50)
    comentarios = models.TextField(null=True, blank=True)
    estado_venta = models.CharField(max_length=50)
    descuento = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    motivo = models.TextField(null=True, blank=True)
    devolucion = models.TextField(null=True, blank=True)
    nombre_calendario = models.CharField(max_length=255, null=True, blank=True)
    pdf = models.FileField(upload_to='pdfs/', null=True, blank=True)
    identificacion = models.ImageField(upload_to='identificaciones/', null=True, blank=True)
    identificacion_trasera = models.ImageField(upload_to='identificaciones/', null=True, blank=True)
    coste_fotos = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    tiara = models.CharField(max_length=50, choices=[('Entregada', 'Entregada'), ('No entregada', 'No entregada'), ('Sin tiara', 'Sin tiara')], null=True, blank=True)
    cancan = models.CharField(max_length=50, choices=[('3 aros', '3 aros'), ('6 aros', '6 aros'), ('8 aros', '8 aros')], null=True, blank=True)
    fecha_extra_fotos = models.DateField(null=True, blank=True)
    compras = models.TextField(null=True, blank=True)
    history = HistoricalRecords()

    def __str__(self):
        return f"Venta {self.id_ventas} - {self.tienda}"

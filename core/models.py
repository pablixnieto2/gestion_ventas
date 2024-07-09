from django.db import models

class Cliente(models.Model):
    id_cliente = models.CharField(max_length=20, unique=True, default="UNIQUEID")
    created_by = models.EmailField()
    creation_date = models.DateTimeField(auto_now_add=True)
    fecha_fiesta = models.DateField()
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    prefijo = models.CharField(max_length=3, choices=[('+34', '+34'), ('+1', '+1'), ('+44', '+44')])
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    ubicacion = models.CharField(max_length=50, choices=[('Madrid', 'Madrid'), ('Barcelona', 'Barcelona'), ('Valencia', 'Valencia'), ('Videollamada', 'Videollamada')])
    estado = models.CharField(max_length=50, choices=[('sin cita', 'Sin Cita'), ('con cita', 'Con Cita'), ('perdido', 'Perdido'), ('eliminar cliente duplicado', 'Eliminar Cliente Duplicado')])
    como_nos_conocio = models.CharField(max_length=50, choices=[('Google', 'Google'), ('Google maps', 'Google Maps'), ('Instagram', 'Instagram'), ('Facebook', 'Facebook'), ('Recomendación', 'Recomendación'), ('Milanuncios', 'Milanuncios'), ('Web', 'Web'), ('Otro', 'Otro')])
    comentarios = models.TextField(blank=True, null=True)
    vendedora = models.CharField(max_length=100, blank=True, null=True)
    estado_cliente = models.CharField(max_length=50, choices=[('ya compró', 'Ya Compró'), ('perdido', 'Perdido'),('Con Cita', 'Con Cita'),], default='Con Cita')

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.telefono}"

class Producto(models.Model):
    id_producto = models.CharField(max_length=20, unique=True, default="UNIQUEID")
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50, choices=[('Vestido', 'Vestido'), ('Vestido Corto', 'Vestido Corto'), ('Accesorios', 'Accesorios'), ('Complementos', 'Complementos'), ('Envio', 'Envio'), ('Invitaciones', 'Invitaciones'), ('Paquete Fotos', 'Paquete Fotos'), ('Recuerdos', 'Recuerdos'), ('Otros', 'Otros')])
    color = models.CharField(max_length=50)
    talla = models.CharField(max_length=10)
    pvp = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.URLField(blank=True, null=True)
    estado = models.CharField(max_length=50, choices=[('Activo', 'Activo'), ('Baja', 'Baja')])
    tienda = models.CharField(max_length=50, choices=[('Madrid', 'Madrid'), ('Barcelona', 'Barcelona'), ('Valencia', 'Valencia'), ('Videollamada', 'Videollamada')])
    cantidad_madrid = models.IntegerField(default=0)
    cantidad_barcelona = models.IntegerField(default=0)
    cantidad_valencia = models.IntegerField(default=0)
    cantidad_videollamada = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.nombre} - {self.color} - {self.talla}"

class Venta(models.Model):
    id_venta = models.CharField(max_length=20, unique=True, default="UNIQUEID")
    created_by = models.EmailField()
    creation_date = models.DateTimeField(auto_now_add=True)
    tienda = models.CharField(max_length=50, choices=[('Madrid', 'Madrid'), ('Barcelona', 'Barcelona'), ('Valencia', 'Valencia'), ('Videollamada', 'Videollamada')])
    envio_entrega = models.BooleanField(default=False)
    estado_entrega = models.CharField(max_length=50, choices=[('Por Entregar o Enviar', 'Por Entregar o Enviar'), ('Entregado o Enviado', 'Entregado o Enviado'), ('Vestido Devuelto', 'Vestido Devuelto')])
    tipo = models.CharField(max_length=50, choices=[('Alquiler', 'Alquiler'), ('Venta', 'Venta')])
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_entrega = models.DateField()
    fecha_devolucion = models.DateField(blank=True, null=True)
    total_pagar = models.DecimalField(max_digits=10, decimal_places=2)
    total_pagado = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    pendiente_pago = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Venta {self.id_venta} - {self.cliente.nombre} {self.cliente.apellido}"

class VentaProducto(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)

class Pago(models.Model):
    id_pago = models.CharField(max_length=20, unique=True, default="UNIQUEID")
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    created_by = models.EmailField()
    creation_date = models.DateTimeField(auto_now_add=True)
    tienda = models.CharField(max_length=50, choices=[('Madrid', 'Madrid'), ('Barcelona', 'Barcelona'), ('Valencia', 'Valencia'), ('Videollamada', 'Videollamada')])
    metodo_pago = models.CharField(max_length=50, choices=[('Efectivo', 'Efectivo'), ('Tarjeta', 'Tarjeta'), ('BBVA', 'BBVA'), ('SumUp', 'SumUp'), ('Bizum', 'Bizum'), ('Transferencia', 'Transferencia'), ('Paypal', 'Paypal'), ('Web', 'Web')])
    importe = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Pago {self.id_pago} - Venta {self.venta.id_venta}"

# Nuevos Modelos
class Pedido(models.Model):
    id = models.AutoField(primary_key=True)
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    estado_pedido = models.CharField(max_length=50)  # Aquí estaba el error

    def __str__(self):
        return f"Pedido {self.id} - Venta {self.venta.id_venta}"

class SesionFoto(models.Model):
    id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_sesion = models.DateTimeField(auto_now_add=True)
    estado_sesion = models.CharField(max_length=50)  # Aquí estaba el error

    def __str__(self):
        return f"SesionFoto {self.id} - Cliente {self.cliente.nombre}"

class LogSesion(models.Model):
    id = models.AutoField(primary_key=True)
    sesion_foto = models.ForeignKey(SesionFoto, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    accion = models.CharField(max_length=50)  # Aquí estaba el error

    def __str__(self):
        return f"LogSesion {self.id} - SesionFoto {self.sesion_foto.id}"
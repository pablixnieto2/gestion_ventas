from django.db import models
from simple_history.models import HistoricalRecords
from ventas.models import Venta

class Cliente(models.Model):
    id_clientes = models.CharField(max_length=6, unique=True)
    created_by = models.EmailField()
    creation_date = models.DateTimeField(auto_now_add=True)
    fecha_fiesta = models.DateField()
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

class Venta(models.Model):
    id_ventas = models.CharField(max_length=6, unique=True)
    created_by = models.EmailField()
    creation_date = models.DateTimeField(auto_now_add=True)
    change_timestamp = models.DateTimeField(auto_now=True)
    tienda = models.CharField(max_length=20, choices=[('Madrid', 'Madrid'), ('Barcelona', 'Barcelona'), ('Valencia', 'Valencia'), ('Videollamada', 'Videollamada')])
    envio_entrega = models.BooleanField(default=False)
    estado_entrega = models.CharField(max_length=50, choices=[('Por Entregar o Enviar', 'Por Entregar o Enviar'), ('Entregado o Enviado', 'Entregado o Enviado'), ('Vestido Devuelto', 'Vestido Devuelto')])
    tipo = models.CharField(max_length=20, choices=[('Alquiler', 'Alquiler'), ('Venta', 'Venta')])
    id_clientes = models.ForeignKey('clientes.Cliente', on_delete=models.CASCADE)
    id_productos = models.ManyToManyField('productos.Producto')
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

class VentaProducto(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    history = HistoricalRecords()

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

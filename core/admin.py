from django.contrib import admin
from .models import Cliente, Producto, Venta, Pago, Pedido, SesionFoto, LogSesion

# Registro de modelos para el panel de administración de Django
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id_cliente', 'nombre', 'apellido', 'telefono', 'email', 'ubicacion', 'estado')  # Cambié 'id' a 'id_cliente'
    search_fields = ('nombre', 'apellido', 'telefono', 'email')
    list_filter = ('ubicacion', 'estado')

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id_producto', 'nombre', 'categoria', 'pvp', 'estado')  # Cambié 'id' a 'id_producto' y 'precio' a 'pvp'
    search_fields = ('nombre', 'categoria')
    list_filter = ('categoria', 'estado')

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('id_venta', 'cliente', 'fecha_entrega', 'estado_entrega', 'total_pagar', 'total_pagado', 'pendiente_pago')  # Cambié 'id' a 'id_venta', 'total_a_pagar' a 'total_pagar' y 'pendiente_de_pago' a 'pendiente_pago'
    search_fields = ('cliente__nombre', 'cliente__apellido', 'cliente__telefono', 'cliente__email')
    list_filter = ('estado_entrega', 'fecha_entrega')

@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    list_display = ('id_pago', 'venta', 'creation_date', 'metodo_pago', 'importe')  # Cambié 'id' a 'id_pago', 'fecha_creacion' a 'creation_date', 'metodo_de_pago' a 'metodo_pago'
    search_fields = ('venta__id', 'metodo_pago')
    list_filter = ('metodo_pago', 'creation_date')

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'venta', 'fecha_pedido', 'estado_pedido')
    search_fields = ('venta__id', 'estado_pedido')
    list_filter = ('estado_pedido', 'fecha_pedido')

@admin.register(SesionFoto)
class SesionFotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'fecha_sesion', 'estado_sesion')
    search_fields = ('cliente__nombre', 'cliente__apellido', 'cliente__telefono', 'cliente__email')
    list_filter = ('estado_sesion', 'fecha_sesion')

@admin.register(LogSesion)
class LogSesionAdmin(admin.ModelAdmin):
    list_display = ('id', 'sesion_foto', 'timestamp', 'accion')
    search_fields = ('sesion_foto__id', 'accion')
    list_filter = ('timestamp', 'accion')
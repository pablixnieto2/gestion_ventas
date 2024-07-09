from django.test import TestCase
from .models import Cliente, Producto, Venta, VentaProducto, Pago
from django.utils import timezone
from decimal import Decimal

class ClienteModelTest(TestCase):

    def setUp(self):
        self.cliente = Cliente.objects.create(
            id_cliente="C12345",
            created_by="test@example.com",
            fecha_fiesta=timezone.now().date(),
            nombre="Juan",
            apellido="Perez",
            prefijo="+34",
            telefono="123456789",
            email="juan.perez@example.com",
            ubicacion="Madrid",
            estado="sin cita",
            como_nos_conocio="Google",
            comentarios="Cliente potencial",
            vendedora="Ana"
        )

    def test_cliente_creation(self):
        self.assertEqual(self.cliente.nombre, "Juan")
        self.assertEqual(self.cliente.apellido, "Perez")
        self.assertEqual(self.cliente.prefijo, "+34")
        self.assertEqual(self.cliente.telefono, "123456789")
        self.assertEqual(self.cliente.email, "juan.perez@example.com")

class ProductoModelTest(TestCase):

    def setUp(self):
        self.producto = Producto.objects.create(
            id_producto="P12345",
            nombre="Vestido de Fiesta",
            categoria="Vestido",
            color="Rojo",
            talla="M",
            pvp=Decimal('199.99'),
            estado="Activo",
            tienda="Madrid",
            cantidad_madrid=10,
            cantidad_barcelona=5,
            cantidad_valencia=0,
            cantidad_videollamada=2
        )

    def test_producto_creation(self):
        self.assertEqual(self.producto.nombre, "Vestido de Fiesta")
        self.assertEqual(self.producto.categoria, "Vestido")
        self.assertEqual(self.producto.color, "Rojo")
        self.assertEqual(self.producto.talla, "M")
        self.assertEqual(self.producto.pvp, Decimal('199.99'))

class VentaModelTest(TestCase):

    def setUp(self):
        self.cliente = Cliente.objects.create(
            id_cliente="C12346",
            created_by="test2@example.com",
            fecha_fiesta=timezone.now().date(),
            nombre="Maria",
            apellido="Lopez",
            prefijo="+34",
            telefono="987654321",
            email="maria.lopez@example.com",
            ubicacion="Barcelona",
            estado="con cita",
            como_nos_conocio="Instagram",
            comentarios="Cliente recurrente",
            vendedora="Laura"
        )
        self.venta = Venta.objects.create(
            id_venta="V12345",
            created_by="admin@example.com",
            tienda="Madrid",
            envio_entrega=True,
            estado_entrega="Por Entregar o Enviar",
            tipo="Venta",
            cliente=self.cliente,
            fecha_entrega=timezone.now().date(),
            total_pagar=Decimal('299.99'),
            total_pagado=Decimal('100.00'),
            pendiente_pago=Decimal('199.99')
        )

    def test_venta_creation(self):
        self.assertEqual(self.venta.tienda, "Madrid")
        self.assertEqual(self.venta.envio_entrega, True)
        self.assertEqual(self.venta.estado_entrega, "Por Entregar o Enviar")
        self.assertEqual(self.venta.tipo, "Venta")
        self.assertEqual(self.venta.total_pagar, Decimal('299.99'))
        self.assertEqual(self.venta.total_pagado, Decimal('100.00'))
        self.assertEqual(self.venta.pendiente_pago, Decimal('199.99'))

class PagoModelTest(TestCase):

    def setUp(self):
        self.cliente = Cliente.objects.create(
            id_cliente="C12347",
            created_by="test3@example.com",
            fecha_fiesta=timezone.now().date(),
            nombre="Carlos",
            apellido="Garcia",
            prefijo="+1",
            telefono="111222333",
            email="carlos.garcia@example.com",
            ubicacion="Valencia",
            estado="sin cita",
            como_nos_conocio="Facebook",
            comentarios="Cliente nuevo",
            vendedora="Elena"
        )
        self.venta = Venta.objects.create(
            id_venta="V12346",
            created_by="admin@example.com",
            tienda="Valencia",
            envio_entrega=False,
            estado_entrega="Entregado o Enviado",
            tipo="Alquiler",
            cliente=self.cliente,
            fecha_entrega=timezone.now().date(),
            total_pagar=Decimal('399.99'),
            total_pagado=Decimal('399.99'),
            pendiente_pago=Decimal('0.00')
        )
        self.pago = Pago.objects.create(
            id_pago="P12345",
            venta=self.venta,
            created_by="admin@example.com",
            tienda="Valencia",
            metodo_pago="Tarjeta",
            importe=Decimal('399.99')
        )

    def test_pago_creation(self):
        self.assertEqual(self.pago.tienda, "Valencia")
        self.assertEqual(self.pago.metodo_pago, "Tarjeta")
        self.assertEqual(self.pago.importe, Decimal('399.99'))

class VentaProductoModelTest(TestCase):

    def setUp(self):
        self.cliente = Cliente.objects.create(
            id_cliente="C12348",
            created_by="test4@example.com",
            fecha_fiesta=timezone.now().date(),
            nombre="Laura",
            apellido="Martinez",
            prefijo="+44",
            telefono="444555666",
            email="laura.martinez@example.com",
            ubicacion="Madrid",
            estado="con cita",
            como_nos_conocio="Recomendación",
            comentarios="Cliente de confianza",
            vendedora="Paula"
        )
        self.producto = Producto.objects.create(
            id_producto="P12346",
            nombre="Zapatos de Fiesta",
            categoria="Complementos",
            color="Negro",
            talla="38",
            pvp=Decimal('49.99'),
            estado="Activo",
            tienda="Madrid",
            cantidad_madrid=15,
            cantidad_barcelona=0,
            cantidad_valencia=0,
            cantidad_videollamada=1
        )
        self.venta = Venta.objects.create(
            id_venta="V12347",
            created_by="admin@example.com",
            tienda="Madrid",
            envio_entrega=True,
            estado_entrega="Por Entregar o Enviar",
            tipo="Venta",
            cliente=self.cliente,
            fecha_entrega=timezone.now().date(),
            total_pagar=Decimal('49.99'),
            total_pagado=Decimal('49.99'),
            pendiente_pago=Decimal('0.00')
        )
        self.venta_producto = VentaProducto.objects.create(
            venta=self.venta,
            producto=self.producto,
            cantidad=2
        )

    def test_venta_producto_creation(self):
        self.assertEqual(self.venta_producto.cantidad, 2)
        self.assertEqual(self.venta_producto.producto.nombre, "Zapatos de Fiesta")

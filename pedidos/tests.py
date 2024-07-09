from django.test import TestCase
from .models import Pedido
from ventas.models import Venta

class PedidoModelTest(TestCase):

    def setUp(self):
        venta = Venta.objects.create(id_ventas="V12345", created_by="test@example.com", tienda="Madrid")
        Pedido.objects.create(id_pedido="D12345", id_ventas=venta, proveedor="Proveedor A")

    def test_pedido_creation(self):
        pedido = Pedido.objects.get(id_pedido="D12345")
        self.assertEqual(pedido.proveedor, "Proveedor A")

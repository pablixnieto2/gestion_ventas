from django.test import TestCase
from .models import Pago
from ventas.models import Venta

class PagoModelTest(TestCase):

    def setUp(self):
        venta = Venta.objects.create(id_ventas="V12345", created_by="test@example.com", tienda="Madrid")
        Pago.objects.create(id_pago="P12345", id_ventas=venta, metodo_de_pago="Efectivo", importe=100.0)

    def test_pago_creation(self):
        pago = Pago.objects.get(id_pago="P12345")
        self.assertEqual(pago.importe, 100.0)

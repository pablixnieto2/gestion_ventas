from django.test import TestCase
from .models import Venta

class VentaModelTest(TestCase):

    def setUp(self):
        Venta.objects.create(id_ventas="V12345", created_by="test@example.com", tienda="Madrid")

    def test_venta_creation(self):
        venta = Venta.objects.get(id_ventas="V12345")
        self.assertEqual(venta.tienda, "Madrid")

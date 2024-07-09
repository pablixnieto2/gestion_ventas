from django.test import TestCase
from .models import SesionFoto
from ventas.models import Venta

class SesionFotoModelTest(TestCase):

    def setUp(self):
        venta = Venta.objects.create(id_ventas="V12345", created_by="test@example.com", tienda="Madrid")
        SesionFoto.objects.create(id_sesion="S12345", id_ventas=venta, lugar_sesion="Parque")

    def test_sesion_foto_creation(self):
        sesion_foto = SesionFoto.objects.get(id_sesion="S12345")
        self.assertEqual(sesion_foto.lugar_sesion, "Parque")

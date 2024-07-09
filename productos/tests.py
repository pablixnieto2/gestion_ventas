from django.test import TestCase
from .models import Producto

class ProductoModelTest(TestCase):

    def setUp(self):
        Producto.objects.create(id_productos="P12345", nombre="Vestido", categoria="Vestido")

    def test_producto_creation(self):
        producto = Producto.objects.get(id_productos="P12345")
        self.assertEqual(producto.nombre, "Vestido")

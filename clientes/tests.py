from django.test import TestCase
from .models import Cliente

class ClienteModelTest(TestCase):

    def setUp(self):
        Cliente.objects.create(id_clientes="C12345", nombre="Juan", apellido="Pérez")

    def test_cliente_creation(self):
        cliente = Cliente.objects.get(id_clientes="C12345")
        self.assertEqual(cliente.nombre, "Juan")

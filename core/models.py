from django.db import models

class Configuracion(models.Model):
    clave = models.CharField(maxlength=50, unique=True)
    valor = models.CharField(maxlength=255)

    def __str__(self):
        return f"{self.clave}: {self.valor}"

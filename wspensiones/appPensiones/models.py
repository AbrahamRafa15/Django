from django.db import models

# Create your models here.
class Pensionado(models.Model):
    nombre = models.CharField(max_length=200)
    edad = models.IntegerField(default=0)
    edadRetiro = models.IntegerField(default=70)
    saldo = models.FloatField(default=500000.0)
    ahorro = models.FloatField(default=10000.0)
    genero = models.BooleanField(default=False)

    def __str__(self):
        return str(self.nombre)
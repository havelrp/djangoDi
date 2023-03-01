from django.db import models

class Modelo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    dimension = models.CharField(max_length=50)
    material = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre + ' ' + self.descripcion
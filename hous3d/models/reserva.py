from django.db import models

class Reserva(models.Model):
    id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    modelo = models.ForeignKey('Modelo', on_delete=models.CASCADE)
    fecha = models.DateField()
    cantidad = models.IntegerField()
    precio = models.IntegerField()

    def __str__(self):
        return self.cliente + ' ' + self.modelo
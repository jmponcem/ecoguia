from django.db import models


class Consulta(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    confirmarcorreo = models.CharField(max_length=100, default='')
    rut = models.CharField(max_length=100)
    telefono = models.IntegerField()
    asunto = models.CharField(max_length=100)    
    mensaje = models.CharField(max_length=1000)

    def __str__(self):
           return self.nombre


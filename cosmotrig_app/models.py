# Create your models here.
# cosmotrig_app/models.py
from django.db import models

class Historia(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='historias/', null=True, blank=True)

    def __str__(self):
        return self.titulo

class CalculoTrig(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.titulo

class Simulacion(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    modelo_3d = models.FileField(upload_to='modelos_3d/', null=True, blank=True)

    def __str__(self):
        return self.nombre

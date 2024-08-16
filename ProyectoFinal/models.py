from django.db import models


# Create your models here.
class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15, blank=True)
    mensaje = models.TextField()

    def __str__(self):
        return f"Mensaje de {self.nombre}"

class Empleo(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    telefono = models.CharField(max_length=20)

class Formulario(models.Model):
    nombre = models.CharField(max_length=30)
    email = models.EmailField(max_length=40)
    consulta = models.BooleanField()

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Disco(models.Model):
    interprete = models.CharField(max_length=100)
    titulo = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    año_lanzamiento = models.IntegerField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    imagen = models.ImageField(upload_to='discos/', null=True, blank=True)

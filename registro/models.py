from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Commented code
class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    rut = models.CharField(primary_key=True, max_length=12)
    telefono = models.CharField(max_length=12)
    direccion = models.CharField(max_length=100)
    pais = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    comuna = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre 

class Pais(models.Model):
    id_pais = models.AutoField(primary_key=True)
    nombre_pais = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.id_pais} - {self.nombre_pais}"
    
class Region(models.Model):
    id_region = models.AutoField(primary_key=True)
    nombre_region = models.CharField(max_length=100)
    id_pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.id_pais} - {self.id_region} - {self.nombre_region}"
    
class Comuna(models.Model):
    id_comuna = models.AutoField(primary_key=True)
    nombre_comuna = models.CharField(max_length=100)
    id_region = models.ForeignKey(Region, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.id_region} - {self.id_comuna} - {self.nombre_comuna}"
    



from turtle import color
from django.db import models

# Create your models here.


class Macetero(models.Model):
    idMacetero = models.IntegerField(primary_key=True, verbose_name="Id de macetero")
    colorMacetero = models.CharField(max_length= 50, verbose_name="Color de Macetero")

def __str__(self):
    return self.colorMacetero


class Sustrato(models.Model):
    idSustrato = models.IntegerField(primary_key=True, verbose_name="Id de sustrato")
    tipoSustrato = models.CharField(max_length= 50, verbose_name="Tipo de Macetero")

def __str__(self):
    return self.tipoSustrato




class Flor(models.Model):
    idFlor = models.IntegerField(primary_key=True, verbose_name="Id de flor")
    nombreFlor = models.CharField(max_length= 50, verbose_name="Nombre de Flor")

def __str__(self):
    return self.tipoFlor

class Arbusto(models.Model):
    idArbusto = models.IntegerField(primary_key=True, verbose_name="Id de Arbusto")
    nombreArbusto = models.CharField(max_length= 50, verbose_name="Nombre de Arbusto")

def __str__(self):
    return self.nombreArbusto


class Cliente (models.Model):
    rut = models.CharField(primary_key=True, max_length= 10, verbose_name="Rut")
    nombreCompleto = models.CharField(max_length= 200, verbose_name="Nombre de Cliente")
    email = models.EmailField(max_length=100,verbose_name="Email")
    contrasena = models.CharField(max_length=20,verbose_name="Contraseña de Cliente")
    telefono = models.IntegerField(verbose_name="Telefono")
    ciudad = models.CharField(max_length = 100, verbose_name="Ciudad")
    comentario = models.TextField(verbose_name="Comentario")

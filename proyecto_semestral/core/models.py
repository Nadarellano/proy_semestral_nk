
from ast import Store
from turtle import color
from django.db import models

# Create your models here.


class Macetero(models.Model):
    idMacetero = models.IntegerField(primary_key=True, verbose_name="Id de macetero")
    colorMacetero = models.CharField(max_length= 50, verbose_name="Color de macetero")
    precioMacetero = models.IntegerField(default=0, max_digits=9,verbose_name='Precio de macetero')
    stockMacetero = models.IntegerField(default=0, verbose_name="Stock de macetero")

def __str__(self):
    return self.colorMacetero

def __str__(self):
    return self.precioMacetero

def __str__(self):
    return self.stockMacetero


class Sustrato(models.Model):
    idSustrato = models.IntegerField(primary_key=True, verbose_name="Id de sustrato")
    tipoSustrato = models.CharField(max_length= 50, verbose_name="Tipo de sustrato")
    precioSustrato = models.IntegerField(default=0, max_digits=9,verbose_name='Precio de sustrato')
    stockSustrato = models.IntegerField(default=0, verbose_name="Stock de sustrato")

def __str__(self):
    return self.tipoSustrato

def __str__(self):
    return self.precioSustrato

def __str__(self):
    return self.stockSustrato



class Flor(models.Model):
    idFlor = models.IntegerField(primary_key=True, verbose_name="Id de flor")
    nombreFlor = models.CharField(max_length= 50, verbose_name="Nombre de flor")
    precioFlor = models.IntegerField(default=0, max_digits=9,verbose_name='Precio de flor')
    stockFlor = models.IntegerField(default=0, verbose_name="Stock de flor")

def __str__(self):
    return self.tipoFlor

def __str__(self):
    return self.precioFlor

def __str__(self):
    return self.stockFlor

class Arbusto(models.Model):
    idArbusto = models.IntegerField(primary_key=True, verbose_name="Id de arbusto")
    nombreArbusto = models.CharField(max_length= 50, verbose_name="Nombre de arbusto")
    precioArbusto = models.IntegerField(default=0, max_digits=9,verbose_name='Precio de arbusto')
    stockArbusto = models.IntegerField(default=0, verbose_name="Stock de arbusto")

def __str__(self):
    return self.nombreArbusto

def __str__(self):
    return self.precioArbusto

def __str__(self):
    return self.stockArbusto

class Cliente (models.Model):
    rut = models.CharField(primary_key=True, max_length= 10, verbose_name="Rut")
    nombreCompleto = models.CharField(max_length= 200, verbose_name="Nombre de Cliente")
    email = models.EmailField(max_length=100,verbose_name="Email")
    contrasena = models.CharField(max_length=20,verbose_name="Contraseña de Cliente")
    telefono = models.IntegerField(verbose_name="Telefono")
    direccion = models.CharField(max_length=400,verbose_name="Dirección")
    ciudad = models.CharField(max_length = 100, verbose_name="Ciudad")
    fechaRegistro = models.DateField(verbose_name="Fecha de registro de Cliente")
    comentario = models.TextField(verbose_name="Comentario")


def __str__(self):
    return self.nombreCompleto

def __str__(self):
    return self.email

def __str__(self):
    return self.contrasena

def __str__(self):
    return self.telefono

def __str__(self):
    return self.direccion

def __str__(self):
    return self.ciudad
    
def __str__(self):
    return self.comentario


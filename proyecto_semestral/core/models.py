from turtle import color
from django.db import models

# Create your models here.


class Macetero(models.Model):
    idMacetero = models.IntegerField(primary_key=True, verbose_name="Id de macetero")
    colorMacetero = models.CharField(max_length= 50, verbose_name="Color de Macetero")
    stockMacetero = models.IntegerField(default=0, verbose_name="Stock de Macetero")
    precioMacetero = models.IntegerField(default=0, verbose_name="Precio de Macetero")

def __str__(self):
    return self.colorMacetero



class Sustrato(models.Model):
    idSustrato = models.IntegerField(primary_key=True, verbose_name="Id de sustrato")
    tipoSustrato = models.CharField(max_length= 50, verbose_name="Tipo de Sustrato")
    stockSustrato = models.IntegerField(default=0, verbose_name="Stock de Sustrato")
    precioSustrato = models.IntegerField(default=0, verbose_name="Precio de Sustrato")

def __str__(self):
    return self.nombreSustrato




class Flor(models.Model):
    idFlor = models.IntegerField(primary_key=True, verbose_name="Id de flor")
    nombreFlor = models.CharField(max_length= 50, verbose_name="Nombre de Flor")
    stockFlor = models.IntegerField(default=0, verbose_name="Stock de Flor")
    precioFlor = models.IntegerField(default=0, verbose_name="Precio de Flor")
   

def __str__(self):
    return self.nombreFlor


class Arbusto(models.Model):
    idArbusto = models.IntegerField(primary_key=True, verbose_name="Id de Arbusto")
    nombreArbusto = models.CharField(max_length= 50, verbose_name="Nombre de Arbusto")
    stockArbusto = models.IntegerField(default=0, verbose_name="Stock de Arbusto")
    precioArbusto= models.IntegerField(default=0, verbose_name="Precio de Arbusto")

def __str__(self):
    return self.nombreArbusto



class Cliente (models.Model):
    rut = models.CharField(primary_key=True, max_length= 10, verbose_name="Rut")
    nombreCompleto = models.CharField(max_length= 200, verbose_name="Nombre de Cliente")
    email = models.CharField(max_length=100,verbose_name="Email")
    contrasena = models.CharField(max_length=20,verbose_name="Contraseña de Cliente")
    telefono = models.IntegerField(verbose_name="Telefono")
    ciudad = models.CharField(max_length = 100, verbose_name="Ciudad")
    comentario = models.TextField(verbose_name="Comentario")
    direccion = models.CharField(max_length = 300, verbose_name="Dirección")
    fechaRegistro = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de registro")
    ultimaModificacion = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")

#Se mostrará con el nombreCompleto en el panel de administrador
    def __str__(self):
         return self.nombreCompleto

 








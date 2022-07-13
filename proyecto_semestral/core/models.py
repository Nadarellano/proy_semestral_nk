from email.policy import default
from turtle import color
from django.db import models




# Create your models here.


class Macetero(models.Model):
    idMacetero = models.IntegerField(primary_key=True, verbose_name="Id de macetero")
    colorMacetero = models.CharField(max_length= 50, verbose_name="Color de Macetero")
    stockMacetero = models.IntegerField(default=0, verbose_name="Stock de Macetero")
    precioMacetero = models.IntegerField(default=0, verbose_name="Precio de Macetero")
    imagenMacetero = models.CharField(max_length= 300, verbose_name="Imagen Macetero")

    
    def __str__(self):
        return "%s %s" % (self.idMacetero, self.colorMacetero)



class Sustrato(models.Model):
    idSustrato = models.IntegerField(primary_key=True, verbose_name="Id de sustrato")
    tipoSustrato = models.CharField(max_length= 50, verbose_name="Tipo de Sustrato")
    stockSustrato = models.IntegerField(default=0, verbose_name="Stock de Sustrato")
    precioSustrato = models.IntegerField(default=0, verbose_name="Precio de Sustrato")
    imagenSustrato = models.CharField(max_length= 300, verbose_name="Imagen Sustrato")

    def __str__(self):
        return "%s %s" % (self.idSustrato, self.tipoSustrato)



class Flor(models.Model):
    idFlor = models.IntegerField(primary_key=True, verbose_name="Id de flor")
    nombreFlor = models.CharField(max_length= 50, verbose_name="Nombre de Flor")
    stockFlor = models.IntegerField(default=0, verbose_name="Stock de Flor")
    precioFlor = models.IntegerField(default=0, verbose_name="Precio de Flor")
    imagenFlor = models.CharField(max_length= 300, verbose_name="Imagen flor")


    def __str__(self):
        return '%s %s' % (self.idFlor, self.nombreFlor)


class Arbusto(models.Model):
    idArbusto = models.IntegerField(primary_key=True, verbose_name="Id de Arbusto")
    nombreArbusto = models.CharField(max_length= 50, verbose_name="Nombre de Arbusto")
    stockArbusto = models.IntegerField(default=0, verbose_name="Stock de Arbusto")
    precioArbusto= models.IntegerField(default=0, verbose_name="Precio de Arbusto")
    imagenArbusto = models.CharField(max_length= 300, verbose_name="Imagen Arbusto")

    def __str__(self):
        return '%s %s' % (self.idArbusto, self.nombreArbusto)


class Cliente (models.Model):
    rut = models.CharField(primary_key=True, max_length= 10, verbose_name="Rut")
    nombreCompleto = models.CharField(max_length= 200, verbose_name="Nombre de Cliente")
    email = models.CharField(max_length=100,verbose_name="Email")
    contrasena = models.CharField(max_length=20,verbose_name="Contraseña de Cliente")
    telefono = models.CharField(max_length=20,verbose_name="Telefono")
    ciudad = models.CharField(max_length = 100, verbose_name="Ciudad")
    comentario = models.TextField(verbose_name="Comentario")
    direccion = models.CharField(max_length = 300, verbose_name="Dirección", default=False)




    def __str__(self):
         return '%s ' % (self.nombreCompleto)




# class CategoriaProd(models.Model):
#     idCategoria = models.IntegerField(primary_key=True, verbose_name="Id Categoría")
#     nombre = models.CharField(max_length=50, verbose_name="Nombre Categoría")
#     created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha registro")
#     updated = models.DateTimeField(auto_now_add=True, verbose_name="Fecha modificación")

#     # class Meta:
#     #     verbose_name="categoriaProd"
#     #     verbose_name_plural="categoriasProd"

#     def __str__(self):
#         return self.nombre




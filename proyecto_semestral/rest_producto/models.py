from django.db import models
from django.forms import SlugField
from core.models import *


# Create your models here.

class Categoria(models.Model):
	idCategoria= models.IntegerField(primary_key=True, verbose_name="Id de Categoria")
	nombreCategoria=models.CharField(max_length=250,default=False,  blank=True, verbose_name="Nombre de Categoria")
	

	def __str__(self):
	    return self.nombreCategoria




class Producto(models.Model):
    idProducto = models.IntegerField(primary_key=True, verbose_name="Id de Producto")
 
    nombreProducto = models.CharField(max_length=200, verbose_name="Nombre de Producto")
    precioProducto = models.FloatField()
    digital = models.BooleanField(default=False,null=True, blank=True)
    imagenProducto = models.CharField(null=True, blank=True, max_length= 300, verbose_name="Imagen Producto")
    categoria=models.ForeignKey(Categoria,on_delete=models.CASCADE)

   

    def __str__(self):
	    return self.nombreProducto


class Order(models.Model):
	customer = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100, null=True)

	def __str__(self):
		return str(self.id)
		
	@property
	def shipping(self):
		shipping = False
		orderitems = self.orderitem_set.all()
		for i in orderitems:
			if i.product.digital == False:
				shipping = True
		return shipping

	@property
	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total 

	@property
	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total 

class OrderItem(models.Model):
	product = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	@property
	def get_total(self):
		total = self.product.price * self.quantity
		return total

class ShippingAddress(models.Model):
	customer = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	address = models.CharField(max_length=200, null=False)
	city = models.CharField(max_length=200, null=False)
	state = models.CharField(max_length=200, null=False)
	zipcode = models.CharField(max_length=200, null=False)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.address


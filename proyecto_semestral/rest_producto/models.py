from django.db import models

from core.models import Cliente

# Create your models here.
class Producto(models.Model):
    idProducto = models.IntegerField(primary_key=True, verbose_name="Id de Producto")
    nombreProducto = models.CharField(max_length=200, verbose_name="Nombre de Producto")
    precioProducto = models.FloatField()
    digital = models.BooleanField(default=False,null=True, blank=True)
    imagenProducto = models.CharField(null=True, blank=True, max_length= 300, verbose_name="Imagen Producto")

   

    def __str__(self):
	    return self.nombreProducto



class Order(models.Model):
	cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)
	fecha_order = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	transaccion_id = models.CharField(primary_key=True, max_length=100, null=True)

	def __str__(self):
		return str(self.id)
		
	@property
	def shipping(self):
		shipping = False
		orderitems = self.orderitem_set.all()
		for i in orderitems:
			if i.producto.digital == False:
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
	producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	cantidad_producto = models.IntegerField(default=0, null=True, blank=True)
	fecha_item = models.DateTimeField(auto_now_add=True)

	@property
	def get_total(self):
		total = self.producto.precioProducto * self.cantidad_producto
		return total

class DireccionDespacho(models.Model):
	cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	direccion = models.CharField(max_length=200, null=False)
	ciudad = models.CharField(max_length=200, null=False)
	comuna = models.CharField(max_length=200, null=False)

	def __str__(self):
		return self.direccion
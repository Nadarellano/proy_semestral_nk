from django.conf import settings
from django.urls import path
from .views import  *
from rest_producto.views import *
from core import views
from django.conf.urls.static import static


urlpatterns = [
    path('', index,name='index'),
    path('index', index,name='index'),
    path('carrito', carrito,name='carrito'),
    path('nosotros', nosotros, name='nosotros'),
    path('datos_seguimiento', datos_seguimiento, name='datos_seguimiento'),
    path('pago', pago, name='pago'),
    path('prod_arbustos', prod_arbustos, name='prod_arbustos'),
    path('prod_flores', prod_flores, name='prod_flores'),
    path('prod_maceteros', prod_maceteros, name='prod_maceteros'),
    path('prod_sustratos', prod_sustratos, name='prod_sustratos'),
    path('registrodos', registrodos, name='registrodos'), 
    path('stock', stock, name='stock'),
    path('terminos_condiciones', terminos_condiciones, name='terminos_condiciones'),
    path('ubicacion_compra', ubicacion_compra, name='ubicacion_compra'),
    path('datos_cliente', datos_cliente, name='datos_cliente'),
    path('form_mod_datos/<id>', form_mod_datos, name='form_mod_datos'),
    path('form_del_datos/<id>', form_del_datos, name='form_del_datos'),
    path('contact', contact, name='contact'),
    path('datos_despacho', datos_despacho, name='datos_despacho'),
    path('form_direccion/<id>', form_direccion, name='form_direccion'),
    path('lista_productos', lista_productos, name='lista_productos'),
    path('tienda', tienda, name='tienda'),
   
	path('checkout/', views.checkout, name="checkout"),

	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
    

   

]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
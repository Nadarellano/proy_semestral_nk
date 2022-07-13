import email
from django.urls import path
from rest_producto.views import *
from core.views import *

from django.urls import path

from .import views

app_name="rest_producto"



urlpatterns = [
    path('lista_maceteros', lista_maceteros, name="lista_maceteros"),
    path('lista_arbustos', lista_arbustos, name="lista_arbustos"),
    path('lista_flores', lista_flores, name="lista_flores"),
    path('lista_sustratos', lista_sustratos, name="lista_sustratos"),
    path('lista_clientes', lista_clientes, name="lista_clientes"),
    path('detalle_macetero/<id>', detalle_macetero, name="detalle_macetero"),
    path('detalle_sustrato/<id>', detalle_sustrato, name="detalle_sustrato"),
    path('detalle_arbusto/<id>', detalle_arbusto, name="detalle_arbusto"),
    path('detalle_flor/<id>', detalle_flor, name="detalle_flor"),
    path('detalle_cliente/<id>', detalle_cliente, name="detalle_cliente"),
    path('lista_productos', lista_productos, name="lista_productos"),
    path('detalle_order/<id>', detalle_order, name='detalle_order'),
    path('detalle_order_item/<id>', detalle_order_item, name='detalle_order_item')

    

 
]
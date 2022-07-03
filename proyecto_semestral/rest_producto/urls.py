import email
from django.urls import path
from rest_producto.views import lista_maceteros, lista_arbustos, lista_flores, lista_sustratos, lista_clientes,detalle_macetero,detalle_sustrato,detalle_arbusto,detalle_flor,detalle_cliente
from rest_producto.viewsLogin import login

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
    path('login',login, name="login"),
]
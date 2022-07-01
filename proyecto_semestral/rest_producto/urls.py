from django.urls import path
from rest_producto.views import lista_maceteros, lista_arbustos, lista_flores, lista_sustratos,detalle_macetero

urlpatterns = [
    path('lista_maceteros', lista_maceteros, name="lista_maceteros"),
    path('lista_arbustos', lista_arbustos, name="lista_arbustos"),
    path('lista_flores', lista_flores, name="lista_flores"),
    path('lista_sustratos', lista_sustratos, name="lista_sustratos"),
    path('detalle_macetero/<id>', detalle_macetero, name="detalle_macetero"),
]
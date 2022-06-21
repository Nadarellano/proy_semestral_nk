from django.urls import path
from rest_producto.views import lista_maceteros

urlpatterns = [
    path('lista_maceteros', lista_maceteros, name="lista_maceteros")
]
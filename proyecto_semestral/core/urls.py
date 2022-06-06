from django.urls import path
from .views import index, carrito, nosotros


urlpatterns = [
    path('', index,name='index'),
    path('carrito', carrito,name='carrito'),
    path('nosotros', nosotros, name='nosotros')

    
]
from django.contrib import admin
from .models import *
admin.site.register(Producto)
admin.site.register(Order)
admin.site.register(OrderItem)

admin.site.register(Categoria)

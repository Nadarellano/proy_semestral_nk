from django.contrib import admin
from .models import Cliente,Arbusto,Flor, Macetero, Sustrato, Producto
#  Register your models here.

admin.site.register(Cliente)
admin.site.register(Arbusto)
admin.site.register(Flor)
admin.site.register(Macetero)
admin.site.register(Sustrato)
admin.site.register(Producto)



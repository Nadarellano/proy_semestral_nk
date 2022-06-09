from django.contrib import admin
from .models import Cliente,Arbusto,Flor, Macetero, Sustrato
# Register your models here.


#Para visualizar más campo en el panel de admin

class ClientesAdmin(admin.ModelAdmin):

    list_display=("nombreCompleto", "rut", "email")

#Agrega campo de busqueda en panel de administrador    
search_fields=("rut", "email")

admin.site.register(Cliente, ClientesAdmin)
admin.site.register(Arbusto)
admin.site.register(Flor)
admin.site.register(Macetero)
admin.site.register(Sustrato)


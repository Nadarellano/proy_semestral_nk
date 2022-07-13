from dataclasses import fields
from rest_framework import serializers
from core.models import *
from rest_producto.models import *


class MacSerializer(serializers.ModelSerializer):
    class Meta:
        model = Macetero
        fields = ['idMacetero','colorMacetero','stockMacetero','precioMacetero','imagenMacetero']


class ArbustoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arbusto
        fields = ['idArbusto','nombreArbusto','stockArbusto','precioArbusto','imagenArbusto']

class FlorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flor
        fields = ['idFlor','nombreFlor','stockFlor','precioFlor','imagenFlor']

class SustratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sustrato
        fields = ['idSustrato','tipoSustrato','stockSustrato','precioSustrato','imagenSustrato']


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['rut','nombreCompleto','email','contrasena','telefono','ciudad','comentario','direccion']

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['idProducto','nombreProducto','precioProducto','imagenProducto','categoria']
    
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['cliente', 'fecha_order', 'complete', 'transaccion_id']

class OrderItemSerializer(serializers.ModelSerializer):
    producto = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    order = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = OrderItem
        fields = ['producto', 'order', 'cantidad_producto', 'fecha_item']



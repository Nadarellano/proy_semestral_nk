from rest_framework import serializers
from core.models import Macetero, Sustrato, Arbusto, Flor, Cliente


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
    
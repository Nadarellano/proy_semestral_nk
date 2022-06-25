from rest_framework import serializers
from core.models import Macetero, Sustrato, Arbusto, Flor
from core.models import Arbusto, Flor, Sustrato, Macetero


class MacSerializer(serializers.ModelSerializer):
    class Meta:
        model = Macetero
        fields = ['idMacetero','colorMacetero','stockMacetero','precioMacetero','imagenMacetero', 'detalleMacetero']


class ArbustoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arbusto
        fields = ['idArbusto','nombreArbusto','stockArbusto','precioArbusto','imagenArbusto',  'detalleArbusto']

class FlorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flor
        fields = ['idFlor','nombreFlor','stockFlor','precioFlor','imagenFlor',  'detalleFlor']

class SustratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sustrato
        fields = ['idSustrato','tipoSustrato','stockSustrato','precioSustrato','imagenSustrato',  'detalleSustrato']


    
    
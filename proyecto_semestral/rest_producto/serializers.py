from rest_framework import serializers
from core.models import Macetero

class MacSerializer(serializers.ModelSerializer):
    class Meta:
        model = Macetero
        fields = ['idMacetero','colorMacetero','stockMacetero','precioMacetero','imagenMacetero']
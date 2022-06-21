from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

from core.models import Macetero
from .serializers import MacSerializer

@csrf_exempt
@api_view(['GET', 'POST'])
def lista_maceteros(request):
    if request.method == 'GET':
        maceteros = Macetero.objects.all()
        mac_serializer = MacSerializer(maceteros, many=True)
        return Response(mac_serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        mac_serializer = MacSerializer(data=data)
        if mac_serializer.is_valid():
            mac_serializer.save()
            return Response(mac_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(mac_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

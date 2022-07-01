from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

from core.models import Macetero, Sustrato, Arbusto, Flor
from .serializers import MacSerializer, ArbustoSerializer, FlorSerializer, SustratoSerializer

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


@csrf_exempt
@api_view(['GET', 'POST'])
def lista_arbustos(request):
    if request.method == 'GET':
        arbustos = Arbusto.objects.all()
        arb_serializer = ArbustoSerializer(arbustos, many=True)
        return Response(arb_serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        arb_serializer = ArbustoSerializer(data=data)
        if arb_serializer.is_valid():
            arb_serializer.save()
            return Response(arb_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(arb_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET', 'POST'])
def lista_flores(request):
    if request.method == 'GET':
        flores = Flor.objects.all()
        flor_serializer = FlorSerializer(flores, many=True)
        return Response(flor_serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        flor_serializer = FlorSerializer(data=data)
        if flor_serializer.is_valid():
            flor_serializer.save()
            return Response(flor_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(flor_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET', 'POST'])
def lista_sustratos(request):
    if request.method == 'GET':
        sustratos = Sustrato.objects.all()
        sustrato_serializer = SustratoSerializer(sustratos, many=True)
        return Response(sustrato_serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        sustrato_serializer = SustratoSerializer(data=data)
        if sustrato_serializer.is_valid():
            sustrato_serializer.save()
            return Response(sustrato_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(sustrato_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def detalle_macetero(request,id):
    try:
        macetero = Macetero.objects.get(id=id)
    except Macetero.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    if request.method =='GET':
        mac_serializer = MacSerializer(macetero)
        return Response(mac_serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        mac_serializer = MacSerializer(macetero, data=data)
        if mac_serializer.is_valid():
            mac_serializer.save()
            return Response(mac_serializer.data)
        else:
            return Response(mac_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        macetero.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    




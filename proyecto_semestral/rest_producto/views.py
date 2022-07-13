from django.shortcuts import redirect, render
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import *
from rest_producto import *
from .serializers import *
from rest_producto.models import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render

from django.shortcuts import redirect

from django.shortcuts import render

from django.shortcuts import redirect

from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime
from .models import * 
from .utils import cookieCart, cartData, guestOrder

@csrf_exempt
@api_view(['GET', 'POST'])

def lista_productos(request):
    if request.method == 'GET':
        productos = Producto.objects.all()
        producto_serializer = ProductoSerializer(productos, many=True)
        return Response(producto_serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        producto_serializer = ProductoSerializer(data=data)
        if producto_serializer.is_valid():
            producto_serializer.save()
            return Response(producto_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(producto_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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

@csrf_exempt
@api_view(['GET', 'POST'])

def lista_clientes(request):
    if request.method == 'GET':
        clientes = Cliente.objects.all()
        cliente_serializer = ClienteSerializer(clientes, many=True)
        return Response(cliente_serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        cliente_serializer = ClienteSerializer(data=data)
        if cliente_serializer.is_valid():
            cliente_serializer.save()
            return Response(cliente_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(cliente_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def detalle_macetero(request,id):
    try:
        macetero = Macetero.objects.get(idMacetero=id)
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

@api_view(['GET','PUT','DELETE'])

def detalle_sustrato(request,id):
    try:
        sustrato = Sustrato.objects.get(idSustrato=id)
    except Sustrato.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    if request.method =='GET':
        sus_serializer = SustratoSerializer(sustrato)
        return Response(sus_serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        sus_serializer = SustratoSerializer(sustrato, data=data)
        if sus_serializer.is_valid():
            sus_serializer.save()
            return Response(sus_serializer.data)
        else:
            return Response(sus_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        sustrato.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','PUT','DELETE'])

def detalle_arbusto(request,id):
    try:
        arbusto = Arbusto.objects.get(idArbusto=id)
    except Arbusto.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    if request.method =='GET':
        arb_serializer = ArbustoSerializer(arbusto)
        return Response(arb_serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        arb_serializer = ArbustoSerializer(arbusto, data=data)
        if arb_serializer.is_valid():
            arb_serializer.save()
            return Response(arb_serializer.data)
        else:
            return Response(arb_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        arbusto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','PUT','DELETE'])

def detalle_flor(request,id):
    try:
        flor = Flor.objects.get(idFlor=id)
    except Flor.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    if request.method =='GET':
        flor_serializer = FlorSerializer(flor)
        return Response(flor_serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        flor_serializer = FlorSerializer(flor, data=data)
        if flor_serializer.is_valid():
            flor_serializer.save()
            return Response(flor_serializer.data)
        else:
            return Response(flor_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        flor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','PUT','DELETE'])

def detalle_cliente(request,id):
    try:
        cliente = Cliente.objects.get(email=id)
    except Cliente.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    if request.method =='GET':
        cliente_serializer = ClienteSerializer(cliente)
        return Response(cliente_serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        cliente_serializer = cliente_serializer(cliente, data=data)
        if cliente_serializer.is_valid():
            cliente_serializer.save()
            return Response(cliente_serializer.data)
        else:
            return Response(cliente_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        cliente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET','PUT','DELETE'])

def detalle_order(request,id):
    try:
        order = Order.objects.get(transaccion_id=id)
    except Order.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    if request.method =='GET':
        order_serializer = OrderSerializer(order)
        return Response(order_serializer.order)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        order_serializer = order_serializer(order, data=data)
        if order_serializer.is_valid():
            order_serializer.save()
            return Response(order_serializer.data)
        else:
            return Response(order_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET','PUT','DELETE'])


def detalle_order_item(request,id):
    try:
        orderitems = OrderItem.objects.get(order=id)
    except OrderItem.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    if request.method =='GET':
        orderitem_serializer = OrderItemSerializer(orderitems)
        return Response(orderitem_serializer.orderitems)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        orderitem_serializer = orderitem_serializer(orderitems, data=data)
        if orderitem_serializer.is_valid():
            orderitem_serializer.save()
            return Response(orderitem_serializer.data)
        else:
            return Response(orderitem_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        orderitems.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





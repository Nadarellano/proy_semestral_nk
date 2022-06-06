from socket import fromshare
from dataclasses import field
# from attr import fields_dict
from django import forms
from django.forms import ModelForm
from .models import Cliente


class ClienteForm(ModelForm):

    class Meta:
        model = Cliente
        fields=[ 'rut', 'nombreCompleto',  'email', 'contrasena', 'telefono', 'ciudad', 'comentario']
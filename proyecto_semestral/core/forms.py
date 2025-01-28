from socket import fromshare
from dataclasses import field
# from attr import fields_dict
from django import forms
from django.forms import ModelForm
from .models import Cliente


class ClienteForm(ModelForm):

    class Meta:
        model = Cliente
        fields=[ 'rut', 'nombreCompleto',  'email', 'telefono', 'ciudad', 'comentario']


class DireccionForm(ModelForm):

    class Meta:
        model = Cliente
        fields=[ 'rut', 'email', 'ciudad', 'direccion', 'nombreCompleto']

class ContactForm(forms.Form):
    name = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Escribe tu nombre'}
    ), min_length=3, max_length=100)
    email = forms.EmailField(label="Email", required=True, widget=forms.EmailInput(
        attrs={'class':'form-control', 'placeholder':'Escribe tu email'}
    ), min_length=3, max_length=100)
    content = forms.CharField(label="Contenido", required=True, widget=forms.Textarea(
        attrs={'class':'form-control', 'rows': 6, 'placeholder':'Escribe tu mensaje'}
    ), min_length=10, max_length=1000)


    
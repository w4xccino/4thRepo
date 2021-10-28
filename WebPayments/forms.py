from django import forms
from django.forms import widgets
from .models import Proveedor


class Proveedor(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = [
            'nombre',
            'moneda',
            'ciclo',
            'categoria',
            'recordatorio',
            'telefono',
            'monto'
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder':'Ingrese su nombre'}),
            'moneda': forms.Select(attrs={'class':'browser-default'}),
            'ciclo': forms.Select(attrs={'class':'browser-default'}),
            'categoria': forms.Select(attrs={'class':'browser-default'}),
            'recordatorio': forms.Select(attrs={'class':'browser-default'}),
            'telefono': forms.TextInput(attrs={'placeholder':'Ingrese su telefono'}),
            'monto': forms.TextInput(attrs={'placeholder':'Ingrese su monto de pago'}),
        }
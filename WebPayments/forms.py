from django import forms
from django.forms import widgets
from .models import Proveedor


class Proveedor(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = [
            'nombre',
            'moneda',
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder':'Ingrese su nombre'}),
        }
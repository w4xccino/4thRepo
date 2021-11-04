from django import forms
from django.forms import widgets
from .models import Proveedor


class Proveedor(forms.ModelForm):
    duracion = forms.DateField(
        input_formats=['%d/%m/%Y'],
        widget=forms.DateInput(attrs={
            'class': 'datepicker',
            'data-target': '.datepicker'
        })
    )
    class Meta:
        model = Proveedor
        fields = [
            'nombre',
            'moneda',
            'ciclo',
            'categoria',
            'recordatorio',
            'duracion',
            'telefono',
            'monto',
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
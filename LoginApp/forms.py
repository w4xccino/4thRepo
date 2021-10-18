from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Usuario

class Registro(UserCreationForm):

    email = forms.EmailField()
    direccion = forms.CharField(label='Direccion')
    c_postal = forms.CharField(label='Codigo Postal')
    password1 = forms.CharField(label='Contrasena',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirma Contrasena',widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ['username',
                  'email',
                  'first_name',
                  'last_name',
                  'password1',
                  'password2',
                  'phone',
                  'direccion',
                  'c_postal',]

        help_text = {k:"" for k in fields}

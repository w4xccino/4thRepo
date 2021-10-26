from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import widgets
from .models import Usuario

class Registro(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
    
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
        help_texts = {None}
        widgets = {
            'username' : forms.TextInput(attrs={'placeholder': 'Ingrese su nombre p'}),
            'email' : forms.EmailInput(),
            'first_name' : forms.TextInput(),
            'last_name' : forms.TextInput(),
            'password1' : forms.PasswordInput(),
            'password2' : forms.PasswordInput(),
            'phone' : forms.TextInput(),
            'direccion' : forms.TextInput(),
            'c_postal' : forms.TextInput(),
        }
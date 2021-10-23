from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import Registro

# Create your views here.d
def register(request):
     if request.method == 'POST':
          form = Registro(request.POST)
          if form.is_valid():
               form.save()
               username = form.cleaned_data['username']
               messages.success(request, f"Usuario {username} ha sido creado")
               
     else:
          form = Registro()
     context = {'form' : form}
     return render(request, 'LoginApp/register.html', context) 


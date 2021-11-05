from django.shortcuts import render
from .forms import Proveedor
from django.contrib import messages
from .models import Proveedor as Prov
import datetime


query = Prov.objects.all()
date_time = datetime.datetime.now()
date = date_time.date()
lista = []

for obj in query:
    if obj.alerta == date:
        nombre = str(obj.nombre)
        lista.append(nombre)
context = {'lista':lista}

def base(request):
    return render(request, 'WebPayments/base.html', context)

def index(request):

    return render(request, 'WebPayments/index.html', context)

def alerta(request):
    query = Prov.objects.all()
    date_time = datetime.datetime.now()
    date = date_time.date()
    lista = []

    for obj in query:
        if obj.alerta == date:
            nombre = str(obj.nombre)
            lista.append(nombre)
    context = {'lista':lista}
    print(context)

    return render(request, 'WebPayments/alerta.html', context)


def listarproveedores(request):
    table = Prov.objects.all()
    context = {'table':table,'lista':lista}
    return render(request, 'WebPayments/listarproveedores.html', context)

def proveedores(request):
    fecha = None
    if request.method == 'POST':
        form = Proveedor(request.POST)
        if form.is_valid():
            form.save()
            nombre = form.cleaned_data['nombre']
            messages.success(request, f"Proveedor {nombre} ha sido creado")
    else:
        form = Proveedor()

    context = {'form':form,'fecha':fecha, 'lista':lista}
    return render(request, 'WebPayments/proveedores.html', context)
        
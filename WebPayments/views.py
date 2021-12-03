from django.shortcuts import render
from .forms import Proveedor
from django.contrib import messages
from .models import Proveedor as Prov
from django.db import connection
import datetime


def alerta():
    query = Prov.objects.all()
    date_time = datetime.datetime.now()
    date = date_time.date()
    lista = []  

    for obj in query:
        if obj.alerta == date:
            nombre = str(obj.nombre)
            lista.append(nombre)
    return lista 
def suma():
    cursor = connection.cursor()
    cursor.execute("call suma_provedores()")
    results = cursor.fetchall()
    return results 

def ordenar():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM ordenar")
    results = cursor.fetchall()
    return results 

def base(request):
    context = {'lista':alerta()}
    return render(request, 'WebPayments/base.html',context) 

def index(request):
    context = {'lista':alerta()}
    return render(request, 'WebPayments/index.html',context)

def listarproveedores(request):
    table = Prov.objects.all()
    context = {'table':table,'lista':alerta(), 'suma':suma(),'ordenar':ordenar}
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

    context = {'form':form,'fecha':fecha, 'lista':alerta()}
    return render(request, 'WebPayments/proveedores.html', context)

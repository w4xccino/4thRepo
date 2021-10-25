from django.shortcuts import render
from .forms import Proveedor
from django.contrib import messages


def base(request):
    return render(request, 'WebPayments/base.html')

def index(request):
    return render(request, 'WebPayments/index.html')

def proveedores(request):
    if request.method == 'POST':
        form = Proveedor(request.POST)
        if form.is_valid():
            form.save()
            nombre = form.cleaned_data['nombre']
            messages.success(request, f"Proveedor {nombre} ha sido creado")

    else:
        form = Proveedor()
    context = {'form':form}
    return render(request, 'WebPayments/proveedores.html', context)
        


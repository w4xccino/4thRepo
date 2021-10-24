from django.shortcuts import render
from .forms import Proveedor


def base(request):
    return render(request, 'WebPayments/base.html')

def index(request):
    return render(request, 'WebPayments/index.html')

def proveedores(request):
    form = Proveedor(request.POST)
    if request == 'POST':
        if form.is_valid():
            moneda = form.cleaned_data('moneda')
    else:
        form = Proveedor()
    context = {'form':form}
    return render(request, 'WebPayments/proveedores.html', context)
        


from django.shortcuts import render
def base(request):
    return render(request, 'WebPayments/base.html')
def index(request):
    return render(request, 'WebPayments/index.html')
def proveedores(request):
    return render(request, 'WebPayments/proveedores.html')
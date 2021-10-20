from django.shortcuts import render
def base(request):
    return render(request, 'WebPayments/base.html')
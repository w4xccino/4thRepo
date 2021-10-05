from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.d
def loginpage(request):
     return render(request, 'login.html')


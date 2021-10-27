from django.urls import path
from django.urls.resolvers import URLPattern
from .views import base, index, proveedores, listarproveedores
from django.urls import path
urlpatterns = [
    path("index/", index, name="index"),
    path("proveedores/", proveedores, name="proveedores"),
    path("listarproveedores/", listarproveedores, name="listarproveedores")
]

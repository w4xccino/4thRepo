from django.urls import path
from django.urls.resolvers import URLPattern
from .views import base, index, proveedores
from django.urls import path
urlpatterns = [
    path("base/", base, name="base"), 
    path("index/", index, name="index"),
    path("proveedores/", proveedores, name="proveedores")
]

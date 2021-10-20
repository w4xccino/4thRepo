from django.urls import path
from django.urls.resolvers import URLPattern
from .views import base
from django.urls import path
urlpatterns = [
    path("base/", base, name="base")
]
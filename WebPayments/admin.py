from django.contrib import admin
from django.contrib import admin
from .models import *
# Register your models here.
class MonedaAdmin(admin.ModelAdmin):
    list_display = ('detalles','simbolo')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    
admin.site.register(Proveedor)
admin.site.register(Recordatorio)
admin.site.register(Categoria)
admin.site.register(Moneda,MonedaAdmin)
admin.site.register(Ciclo)


from django.contrib import admin
from .models import *
# Register your models here.
class MonedaAdmin(admin.ModelAdmin):
    list_display = ('detalles','simbolo')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    search_fields = ('detalles',)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('nombre','moneda','ciclo','duracion','categoria','recordatorio', 'telefono','monto')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    search_fields = ('nombre',)
    
admin.site.register(Proveedor, ProveedorAdmin )
admin.site.register(Recordatorio)
admin.site.register(Categoria)
admin.site.register(Moneda,MonedaAdmin)
admin.site.register(Ciclo)


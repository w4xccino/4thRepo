from django.contrib import admin
from .models import Usuario
from django.contrib.auth.admin import UserAdmin


class AdminAccount(UserAdmin):
    list_display = ('username','email','date_joined', 'first_name','last_name','phone','direccion','c_postal','is_superuser')
    search_fields = ('username','email', 'first_name')
    readonly_fields = ('date_joined','last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
admin.site.register(Usuario,AdminAccount)

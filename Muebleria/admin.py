from django.contrib import admin
from .models import Producto
from .models import Proveedores
from .models import Sucursales



admin.site.register (Producto)
admin.site.register (Proveedores)
admin.site.register (Sucursales)
# Register your models here.

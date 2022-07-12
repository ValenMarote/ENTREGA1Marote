from django import forms
from .models import Producto, Proveedores, Sucursales

class ProductoForm(forms.ModelForm):
    class Meta:
        model= Producto
        fields= '__all__'
        
class ProveedoresForm(forms.ModelForm):
    class Meta:
        model= Proveedores
        fields= '__all__'
        
class SucursalesForm(forms.ModelForm):
    class Meta:
        model= Sucursales
        fields= '__all__'
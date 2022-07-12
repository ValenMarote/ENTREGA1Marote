from gettext import Catalog
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Producto
from .forms import ProductoForm
from .models import Sucursales
from .forms import SucursalesForm
from .models import Proveedores
from .forms import ProveedoresForm
from django.db.models import Q
# Create your views here.

def inicio(request):
    return render (request,'inicio.html')

def agregarproducto(request):
  formulario = ProductoForm(request.POST or None, request.FILES)
  if formulario.is_valid():
    formulario.save()
    return redirect('catalogo')
  return render (request,'Catalogo/agregar.html', {'formulario':formulario })

def editar(request, id):
  producto = Producto.objects.get(id=id)
  Formulario = ProductoForm(request.POST or None, request.FILES)
  if Formulario.is_valid() and request.POST:
   Formulario.save()
   return redirect('catalogo')
  return render (request,'Catalogo/editar.html', {'formulario': Formulario})

def eliminar(request, id):
  producto = Producto.objects.get(id=id)
  producto.delete()
  return redirect ('catalogo')

def catalogo(request):
  queryset= request.GET.get('buscar')
  Productos = Producto.objects.filter
  if queryset:
    Productos = Producto.objects.filter(
      Q(titulo__icontains= queryset) |
      Q(descripcion__icontains=queryset)|
      Q(categoria__icontains=queryset)
    ).distinct()
  return render (request,'Catalogo/index.html',{'Productos': Productos})

def info(request):
  
  return render(request,'Catalogo/login.html')

def agregarproveedor(request):
  formulario1 = ProveedoresForm(request.POST or None, request.FILES)
  if formulario1.is_valid():
    formulario1.save()
    return redirect('proveedores')
  return render (request,'Proveedores/agregar.html', {'formulario1':formulario1 })

def eliminarproveedor(request, id):
  proveedor = Proveedores.objects.get(id=id)
  proveedor.delete()
  return redirect ('proveedores')

def proveedores(request):
    queryset= request.GET.get('buscar')
    Proveedors = Proveedores.objects.filter
    if queryset:
      Proveedors = Proveedores.objects.filter(
        Q(nombre__icontains= queryset) |
        Q(empresa__icontains=queryset)|
        Q(productoprov__icontains=queryset)
        ).distinct()
    return render (request,'Proveedores/index.html',{'Proveedors': Proveedors})

def agregarsucursal(request):
  formulario2 = SucursalesForm(request.POST or None, request.FILES)
  if formulario2.is_valid():
    formulario2.save()
    return redirect('sucursales')
  return render (request,'Sucursales/agregar.html', {'formulario2':formulario2 })

def eliminarsucursal(request, id):
  Sucursal = Sucursales.objects.get(id=id)
  Sucursal.delete()
  return redirect ('sucursales')

def sucursales(request):
    queryset= request.GET.get('buscar')
    Sucursals = Sucursales.objects.filter
    if queryset:
      Sucursals = Sucursales.objects.filter(
        Q(direccion__icontains= queryset) |
        Q(empleados__icontains=queryset)
        ).distinct()
    return render (request,'Sucursales/index.html',{'Sucursals': Sucursals})




from gettext import Catalog
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Producto
from .forms import ProductoForm
from django.db.models import Q
# Create your views here.

def inicio(request):
    return render (request,'inicio.html')

def agregar(request):
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
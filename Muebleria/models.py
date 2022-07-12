from ast import Delete
from django.db import models

# Create your models here.
class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=50, verbose_name= 'Titulo')
    categoria = models.CharField(max_length=20, verbose_name= 'Categoria')
    foto = models.ImageField (upload_to = 'imagenes/', null=True, verbose_name= 'Foto') 
    descripcion = models.TextField(null=True, verbose_name='Descripcion')
    
    def __str__(self):
        fila= "Titulo: " + self.titulo + " - " + "Descripcion: " + self.descripcion
        return fila
    
    def delete(self, using=None, keep_parents=False):
        self.foto.storage.delete(self.foto.name)
        super().delete()
        
class Proveedores(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, verbose_name= 'Nombre del proveedor')
    empresa = models.CharField(max_length=20, verbose_name= 'Empresa')
    productoprov = models.CharField(max_length=50, verbose_name='Proveedor de...')
    
    def __str__(self):
        fila1= "Nombre: " + self.nombre
        return fila1

class Sucursales(models.Model):
   id = models.AutoField(primary_key=True)
   direccion = models.CharField(max_length=50, verbose_name= 'Direccion de la sucursal')
   empleados= models.TextField(null=True, verbose_name='Id de los empleados')
   
   def __str__(self):
        fila2= "Sucursal: " + self.direccion
        return fila2

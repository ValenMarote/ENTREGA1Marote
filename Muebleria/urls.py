from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static
urlpatterns= [
    path('', views.inicio, name='inicio'),
    path('catalogo', views.catalogo, name='catalogo'),
    path('agregar/producto', views.agregarproducto, name ="agregar"),
    path('info', views.info, name="info"),
    path('editar', views.editar, name ='editar'),
    path('eliminar/<str:id>', views.eliminar, name='eliminar'),
    path('editar/<str:id>', views.editar, name='editar'),
    path('agregar/proveedores', views.agregarproveedor, name="agregarproveedor"),
    path('eliminarproveedor/<str:id>', views.eliminarproveedor, name='eliminarproveedor'),
    path('proveedores', views.proveedores, name='proveedores'),
    path('agregar/sucursales', views.agregarsucursal, name="agregarsucursal"),
    path('eliminarsucursal/<str:id>', views.eliminarsucursal, name='eliminarsucursal'),
    path('sucursales', views.sucursales, name='sucursales'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
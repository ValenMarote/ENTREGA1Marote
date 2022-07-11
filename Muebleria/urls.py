from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static
urlpatterns= [
    path('', views.inicio, name='inicio'),
    path('catalogo', views.catalogo, name='catalogo'),
    path('agregar', views.agregar, name ="agregar"),
    path('info', views.info, name="info"),
    path('editar', views.editar, name ='editar'),
    path('eliminar/<str:id>', views.eliminar, name='eliminar'),
    path('editar/<str:id>', views.editar, name='editar'),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
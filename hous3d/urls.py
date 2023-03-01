from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .forms import modeloForm

urlpatterns = [
    path('', views.index, name='Indice'),
    path('productos/', views.productos, name='Productos'),
    path('reservas/', views.reservas, name='Reservas'),
    path('registro/', views.registro, name='Registro'),
    path('modeloForm/', views.modeloForm, name='ModeloForm'),
    path('contacto/', views.contacto, name='Contacto'),
]

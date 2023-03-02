from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import *
from .forms import *


# Create your views here.

def index(request):
    return render(request, 'index.html')

def contacto(request):
    return render(request, 'contacto.html')


def productos(request):
    modelos = Modelo.objects.all()
    return render(request, 'productos.html', {'modelos': modelos})


def reservas(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)

        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.precio = reserva.cantidad * reserva.modelo.precio
            reserva.save()
            return redirect('Indice')
    else:
        form = ReservaForm()
    return render(request, 'reserva.html')


def registro(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            registro = form.save(commit=False)
            registro.save()
            return redirect('Cliente')
    return render(request, 'registro.html')


def modeloForm(request):
    if request.method == 'POST':
        form = ModeloForm(request.POST)
        if form.is_valid():
            modelo = form.save(commit=False)
            modelo.save()
            return redirect('Indice')
    else:
        form = ModeloForm()
    return render(request, 'modeloForm.html', {'form': form})

def cliente(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente.html', {'clientes': clientes})

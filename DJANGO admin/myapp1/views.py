from django.shortcuts import render
from .models import Producto

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'myapp1/lista.html', {'productos': productos})

def home(request):  #Vista para corregir el error
    return lista_productos(request)


from django.shortcuts import render
from inicio.models import Sahumerio

def inicio(request):
    return render(request, "inicio.html")

def crear_sahumerio(request, descripcion, precio):
    Sahumerio.objects.create(descripcion=descripcion, precio=precio)
    return render(request, "crear_sahumerio.html")


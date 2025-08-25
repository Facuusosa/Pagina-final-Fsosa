from django.shortcuts import render
from django.http import HttpResponse    

def inicio(request):
    return render(request, r"C:\Users\Facun\OneDrive\Escritorio\Entregafinalfsosa\inicio.html")

    # return HttpResponse("<h1>Hola, este es el inicio de la pagina<h1>")


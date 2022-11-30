from django.shortcuts import render
from .models import Libro,Afiliado,Retiros
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request,"inicio.html")

def libros(request):
    return render(request,"libros.html")

def afiliados(request):
    return render(request,"afiliados.html")

def retiros(request):
    return render(request,"retiros.html")

def librosFormulario(request):
    return render(request, "librosFormulario.html")




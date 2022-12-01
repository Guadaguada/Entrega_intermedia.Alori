from django.shortcuts import render
from .models import Libro,Afiliado,Retiros
from django.http import HttpResponse
from django.shortcuts import render
from AppBiblioteca.forms import LibroForm, AfiliadoForm, RetirosForm
# Create your views here.

def inicio(request):
    return render(request,"inicio.html")

def libros(request):
    if request.method=="POST":
        form=LibroForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            titulito=informacion["titulo"]
            tipoLibro=informacion["tipo"]
            codigoLibro=informacion["codigo"]

            libro1=Libro(titulo=titulito, tipo=tipoLibro, codigo=codigoLibro)
            libro1.save()
            return render(request,"inicio.html",{"mensaje":"Libro cargado correctamente"})
    else:
        formulario=LibroForm()

    return render(request, "libros.html", {"form":formulario})
   
def afiliados(request):

    if request.method=="POST":
        form=AfiliadoForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            nombre=informacion["nombre"]
            email=informacion["email"]

            afiliado1=Afiliado(nombre=nombre,email=email)
            afiliado1.save()

        return render(request, "inicio.html", {"mensaje": "Afiliado cargado correctamente" })
    else:
        formulario=AfiliadoForm()

    return render(request,"afiliados.html",{"form":formulario})


def retiros(request):

    if request.method=="POST":
        form=RetirosForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            codigoLibro=informacion["codigoLibro"]
            nombreAfiliado=informacion["nombreAfiliado"]
            fechaRetiro=informacion["fechaRetiro"]

            retiro1=Retiros(codigoLibro=codigoLibro,nombreAfiliado=nombreAfiliado,fechaRetiro=fechaRetiro)
            retiro1.save()

        return render(request,"inicio.html",{"mensaje":"Retiro registrado correctamente"})

    else:
        formulario=RetirosForm()

    return render(request,"retiros.html", {"form":formulario})

def busquedaLibros(request):
    return render(request, "busquedaLibros.html")

def buscar(request):

    if request.GET["codigo"]:

        codigo=request.GET["codigo"]

        libritos=Libro.objects.filter(codigo=codigo)
        return render(request, "resultadosBusqueda.html", {"libros":libritos})
    else:
        return render(request, "busquedaLibros.html", {"mensaje":"Ingrese el codigo del libro a buscar"})
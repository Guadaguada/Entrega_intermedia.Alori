from django.shortcuts import render
from .models import Libro,Afiliado,Retiros
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
            autorcito=informacion["autor"]
            tipoLibro=informacion["tipo"]
            codigoLibro=informacion["codigo"]

            libro1=Libro(titulo=titulito,autor=autorcito, tipo=tipoLibro, codigo=codigoLibro)
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
            apellido=informacion["apellido"]
            email=informacion["email"]
            retiro=informacion["retiro"]

            afiliado1=Afiliado(nombre=nombre,apellido=apellido,email=email,retiro=retiro)
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

    if "codigo" in request.GET:
    
        codigo=request.GET["codigo"]

        libritos=Libro.objects.filter(codigo__icontains=codigo)
        return render(request, "resultadosBusqueda.html", {"libros":libritos})
    else:
        
        return render(request, "busquedaLibros.html", {"mensaje":"Ingrese el codigo del libro a buscar"})
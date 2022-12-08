from django.http import HttpResponse

def inicio(request):
    saludo="Bienvenido a mi servidor. Ingrese en el url /AppBiblioteca para ingresar"
    return HttpResponse(saludo)
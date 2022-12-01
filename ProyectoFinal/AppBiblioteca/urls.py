from django.urls import path
from AppBiblioteca.views import *

urlpatterns = [
    path("libros/", libros,name="libros"),
    path("afiliados/", afiliados, name="afiliados"),
    path("retiros/", retiros, name="retiros"),
    path("", inicio, name="inicio"),
]
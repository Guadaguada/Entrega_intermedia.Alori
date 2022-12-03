from django.db import models

# Create your models here.

class Libro(models.Model):

    titulo = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    codigo = models.IntegerField()

class Afiliado(models.Model):
    
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email = models.EmailField()
    retiro = models.BooleanField(default=False)
   
class Retiros(models.Model):
    
    codigoLibro =models.IntegerField()
    nombreAfiliado = models.CharField(max_length=50)
    fechaRetiro = models.DateField(auto_now=True)

    

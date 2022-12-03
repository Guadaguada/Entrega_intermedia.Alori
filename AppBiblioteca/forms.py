from django import forms


class LibroForm(forms.Form):
    titulo= forms.CharField(max_length=50)
    autor= forms.CharField(max_length=50)
    tipo= forms.CharField(max_length=50)
    codigo=forms.IntegerField()

class AfiliadoForm(forms.Form):
    
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    email = forms.EmailField()
    retiro = forms.BooleanField(required=False)
   
class RetirosForm(forms.Form):
    
    codigoLibro =forms.IntegerField()
    nombreAfiliado =forms.CharField(max_length=50)
    fechaRetiro = forms.DateField()



from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Producto, Perfil, Direccion, Provincia


class ProductosForms(forms.ModelForm):

    class Meta:
        model = Producto
        fields = 'nombre', 'unidades', 'categoria', 'marca', 'modelo', 'precio', 'detalles', 'imagen'


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['password', 'username']


class RegistroForm1(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class RegistroForm2(ModelForm):
    class Meta:
        model = Perfil
        fields = ['dni', 'telefono']


class RegistroForm3(ModelForm):
    class Meta:
        model = Direccion
        fields = ['direccion', 'localidad', 'provincia', 'codPostal']


class RegistroForm(forms.Form):

    username = forms.CharField()
    password = forms.CharField()

    dni = forms.CharField(max_length=9)
    telefono = forms.CharField(max_length=14)

    direccion = forms.CharField(max_length=70)
    localidad = forms.CharField(max_length=20)
    provincia = forms.ModelChoiceField(queryset=Provincia.objects)
    codPostal = forms.IntegerField()
    #
    # numeroTarjeta = forms.CharField(max_length=16)
    # titular = forms.CharField(max_length=50)
    # cvv = forms.IntegerField(max_value=999)
    # fechaCaducidad = forms.DateField()


class AniadirDireccionForm(forms.Form):
    direccion = forms.CharField(max_length=70)
    localidad = forms.CharField(max_length=20)
    provincia = forms.ModelChoiceField(queryset=Provincia.objects)
    codPostal = forms.IntegerField()


class AniadirTarjetaForm(forms.Form):

    numeroTarjeta = forms.CharField(max_length=16)
    titular = forms.CharField(max_length=50)
    cvv = forms.IntegerField(max_value=999)
    fechaCaducidad = forms.DateField()

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Consulta


# Extendemos del original

class RegisterForm(UserCreationForm):
    # Establecemos que el campo username es tipo email y el nombre
    
    email = forms.EmailField(label="Correo electrónico")
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")

    class Meta:
        model = User
        fields = [ "first_name", "last_name", "username", "email", "password1", "password2" ]

class ConsultaForm(ModelForm):
    class Meta:
        model = Consulta
        fields = ['nombre', 'apellido', 'correo' , 'confirmarcorreo', 'rut' , 'telefono', 'asunto', 'mensaje']

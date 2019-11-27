from django.shortcuts import render, redirect
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from .models import Consulta
from .forms import ConsultaForm

def welcome(request):
    # Si estamos identificados devolvemos la portada
    if request.user.is_authenticated:
        return render(request, "users/welcome.html")
        return redirect('/index')
    # En otro caso redireccionamos al login
    return redirect('/login')


def register(request):
    # Creamos el formulario de autenticación vacío
    form = RegisterForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = RegisterForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():

            # Creamos la nueva cuenta de usuario
            user = form.save()

            # Si el usuario se crea correctamente 
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')

# Si queremos borramos los campos de ayuda
    form.fields['username'].help_text = None
    form.fields['password1'].help_text = None
    form.fields['password2'].help_text = None

    # Si llegamos al final renderizamos el formulario
    return render(request, "users/register.html", {'form': form})


def login(request):
    # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')

    # Si llegamos al final renderizamos el formulario
    return render(request, "users/login.html", {'form': form})

def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')


def index(request):
    consultas = Consulta.objects(all) 
    form = ConsultaForm()
    return render(request, "users/Index.html", {'form': form})
    return render(request, "users/Index.html")
    return redirect('/index')

def add(request):
    # Creamos un formulario vacío
    form = ConsultaForm()

    # Comprobamos si se ha enviado el formulario
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = ConsultaForm(request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Guardamos el formulario pero sin confirmarlo,
            # así conseguiremos una instancia para manejarla
            instancia = form.save(commit=False)
            # Podemos guardarla cuando queramos
            instancia.save()
            # Después de guardar redireccionamos a la lista
            return redirect('/index')

    # Si llegamos al final renderizamos el formulario
    return render(request, "users/Index.html", {'form': form})

def edit(request, consulta_id):
    # Recuperamos la instancia de la persona
    instancia = Consulta.objects.get(id=consulta_id)

    # Creamos el formulario con los datos de la instancia
    form = ConsultaForm(instance=instancia)

    # Comprobamos si se ha enviado el formulario
    if request.method == "POST":
        # Actualizamos el formulario con los datos recibidos
        form = ConsultaForm(request.POST, instance=instancia)
        # Si el formulario es válido...
        if form.is_valid():
            # Guardamos el formulario pero sin confirmarlo,
            # así conseguiremos una instancia para manejarla
            instancia = form.save(commit=False)
            # Podemos guardarla cuando queramos
            instancia.save()

    # Si llegamos al final renderizamos el formulario
    return render(request, "users/edit.html", {'form': form})

def listar(request):
    consultas = Consulta.objects.all()
    form = ConsultaForm()
    return render(request, "users/listar.html", {'consultas': consultas}, {'form': form})

def delete(request, consulta_id):

    # Recuperamos la instancia de la persona y la borramos
    instancia = Consulta.objects.get(id=consulta_id)
    instancia.delete()

    # Después redireccionamos a la lista
    return redirect('/listar')


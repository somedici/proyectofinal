from django.shortcuts import render
from django.http import HttpResponse
from .models import Reserva, Terapeuta
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import ReservaCreateForm, LoginForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import SearchForm

def crear_reserva(request):
    if request.method == "GET":
        contexto = {"create_form": ReservaCreateForm()}
        return render(request, "reservas_form.html", contexto)
    
    elif request.method == 'POST':
        form = ReservaCreateForm(request.POST)
        if form. is_valid ():
            nombre_usuario = form.cleaned_data['nombre_usuario']
            fecha = form.cleaned_data['fecha']
            hora = form.cleaned_data['hora']
            tipo_terapia = form.cleaned_data['tipo_terapia']
            terapeuta = form.cleaned_data['terapeuta']
            nueva_reserva = Reserva(
                nombre_usuario=nombre_usuario, 
                fecha=fecha, 
                hora=hora, 
                tipo_terapia=tipo_terapia, 
                terapeuta=terapeuta)
            nueva_reserva.save()
            return detail_view(request, nueva_reserva.id)
        else:
            contexto = {"create_form": form }
            return render(request, "reservas_form.html", contexto)

def home_view(request):
    return render(request,"home.html")

def terapias_view(request):
       return render(request,"terapias.html") 

def terapeutas(request):
    return render(request, "terapeutas.html")

def login_view(request):
    if request.method == "GET":
        contexto = {"form": LoginForm()}
        return render(request, "login.html", contexto)
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                print("Error al registrarse")
            return HttpResponse("Error: Nombre de usuario o contraseña incorrectos.")

def todas_las_reservas(request):
    reservas = Reserva.objects.all()
    contexto_dict = {"todas_las_reservas": reservas}
    return render(request, "list.html", contexto_dict)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Usuario {username} registrado exitosamente.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')  

def search_view(request, nombre):
    reservas_usuario = Reserva.objects.filter(nombre_usuario=nombre).all()
    contexto_dict = {"reservas": reservas_usuario}
    return render(request, "form_view.html", contexto_dict)

def search_view(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            fecha = form.cleaned_data['fecha']
            tipo_terapia = form.cleaned_data['tipo_terapia']
            # Realizar la búsqueda de terapeutas disponibles según los criterios
            terapeutas_disponibles = Terapeuta.objects.filter(
                reservas_fecha=fecha,
                tipo_terapia=tipo_terapia
            ).distinct()
            return render(request, 'search_results.html', {'terapeutas': terapeutas_disponibles})
    else:
        form = SearchForm()
    return render(request, 'search.html', {'search_form': form})


def base(request):
   return render(request,"about.html")


def detail_view(request, booking_id):
    reserva = Reserva.objects.get(id=booking_id)
    contexto_dict = {"reserva": reserva}
    return render (request,"detail.html", contexto_dict )
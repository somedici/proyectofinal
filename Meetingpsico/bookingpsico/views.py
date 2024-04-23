from django.shortcuts import render
from django.http import HttpResponse
from .models import Reserva, Terapeuta
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import ReservaCreateForm, LoginForm

def crear_reserva(request):
    if request.method == "GET":
        contexto = {"create_form": ReservaCreateForm()}
        return render(request, "reservas.html", contexto)
    
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

def home_view(request):
    return render(request,"home.html")

def terapias_view(request):
       return render(request,"terapias.html") 

def terapeutas(request):
    return render(request, "terapeutas.html")

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
            
                return redirect('/bookingpsico/')
            else:
                print("Error al registrarse")
                pass
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def todas_las_reservas(request):
    reservas = Reserva.objects.all()
    contexto_dict = {"todas_las_reservas": reservas}
    return render(request, "list.html", contexto_dict)

def search_view(request, nombre):
    reservas_usuario = Reserva.objects.filter(nombre_usuario=nombre).all()
    contexto_dict = {"reservas": reservas_usuario}
    return render(request, "list.html", contexto_dict)

def detail_view(request, booking_id):
    reserva = Reserva.objects.get(id=booking_id)
    contexto_dict = {"reserva": reserva}
    return render(request, "detail.html", contexto_dict)
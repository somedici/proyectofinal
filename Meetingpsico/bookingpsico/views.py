from django.shortcuts import render
from django.http import HttpResponse
from .models import Reserva

# En tu archivo views.py
from django.shortcuts import render, redirect
from .models import Reserva  # Importa tu modelo de reserva

def crear_reservas(request):
    if request.method == 'POST':
        nombre_usuario = request.POST['nombre_usuario']
        fecha = request.POST['fecha']
        hora = request.POST['hora']
        tipo_terapia = request.POST['tipo_terapia']
        terapeuta = request.POST['terapeuta']
        
        # Crea una nueva instancia de Reserva y guárdala en la base de datos
        reserva = Reserva(nombre_usuario=nombre_usuario, fecha=fecha, hora=hora, tipo_terapia=tipo_terapia, terapeuta=terapeuta)
        reserva.save()
        # Redirecciona a una página de confirmación o a donde desees
        return redirect('/bookingpsico/')
    
    return render(request, 'reservas.html')

def home_view(request):
    return render(request,"home.html")

def terapias_view(request):
       return render(request,"terapias.html") 

def terapeutas(request):
    return render(request, "terapeutas.html")

def login(request):
    return render(request, "login.html")

def search_view(request, nombre):
    reservas_del_usuario = Reserva.objects.filter(nombre_de_usuario=nombre).all()
    contexto_dict = {"reservas": reservas_del_usuario}
    return render(request, "reservas.html", contexto_dict)



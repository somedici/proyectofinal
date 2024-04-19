from django.shortcuts import render
from django.http import HttpResponse
from .models import Reserva

def reserva(request):
    return render(request, "reservas.html")

def home_view(request):
    return render(request,"home.html")

def terapias_view(request):
    reservas = Reserva.objects.all()
    contexto_dict = {"Reservas": reservas}
    return render(request,"terapias.html", contexto_dict) 

def search_view(request, nombre_de_usuario):
    reservas_del_usuario = Reserva.objects.filter(nombre_de_usuario=nombre_de_usuario).all()
    contexto_dict = {"reservas": reservas_del_usuario}
    return render(request, "reservas.html", contexto_dict)

def create_view(request, nombre_de_usuario, terapia):
    Reserva = Reserva.objects.create(nombre_de_usuario,terapia)
    HttpResponse("<h2>Se ha creado con éxito{reserva}<h1>") 


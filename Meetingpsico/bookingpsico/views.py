from django.shortcuts import render
from django.http import HttpResponse

def home_view(xx):
    return HttpResponse("<h2>Encuentra tu camino hacia el bienestar<h1>") 

def terapias_view(request):
   contexto_dict = {
        "Terapias": ["Terapia Cognitivo-Conductual (TCC)", 
                     "Terapia Psicodinámica", 
                     "Terapia de Pareja:", 
                     "Terapia Familiar",
                     "Terapia de Grupo",
                     "Terapia Gestalt",
                     ]
    }
   return render(request,"terapias.html", contexto_dict) 

def search_view(request):
        return HttpResponse("<h2>Search<h1>") 
 
def create_view(request):
        return HttpResponse("<h2>Encuentra tu camino hacia el bienestar<h1>") 


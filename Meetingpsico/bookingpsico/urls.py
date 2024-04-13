from django.urls import path
from django.http import HttpResponse

from .views import home_view, terapias_view, search_view, create_view

urlpatterns = [
    
    path("", home_view),
    path("terapias/", terapias_view, name = "booking"),
    path("buscar/<nombre_de_usuario>", search_view),
    path("crear/<nombre_de_usuario>/<sala>", create_view),
]
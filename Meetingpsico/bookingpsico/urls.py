from django.urls import path
from django.http import HttpResponse

from .views import home_view, terapias_view, search_view, create_view

urlpatterns = [
    
    path("", home_view, name = "home"),
    path("terapias/", terapias_view, name = "terapias"),
    path("buscar/", search_view, name = "reservas"),
    path("crear/<nombre_de_usuario>/<terapias>", create_view),
]
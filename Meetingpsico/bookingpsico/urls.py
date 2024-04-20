from django.urls import path
from django.http import HttpResponse

from .views import home_view, crear_reservas, terapeutas, login, terapias_view, search_view

urlpatterns = [
    
    path("", home_view, name = "home"),
    path("bookingpsico/login", login, name = "login"),
    path("bookingpsico/reservas/", crear_reservas, name = "reserva"),
    path("bookingpsico/terapias/", terapias_view, name = "terapias"),
    path("bookingpsico/terapeutas", terapeutas, name = "terapeutas"),
    path("bookingpsico/buscar/", search_view, name = "reservas"),
   
]
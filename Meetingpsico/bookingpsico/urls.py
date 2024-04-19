from django.urls import path
from django.http import HttpResponse

from .views import home_view, reserva, terapias_view, search_view, create_view

urlpatterns = [
    
    path("", home_view, name = "home"),
    path("bookingpsico/reservas/", reserva, name = "reserva"),
    path("bookingpsico/terapias/", terapias_view, name = "terapias"),
    path("bookingpsico/buscar/", search_view, name = "reservas"),
    path("bookingpsico/crear/<nombre_de_usuario>/<terapias>", create_view),
]
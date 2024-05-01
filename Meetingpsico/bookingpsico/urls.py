from django.urls import path
from django.http import HttpResponse

from .views import home_view, crear_reserva, terapeutas,login_view, terapias_view, detail_view, search_view, todas_las_reservas, register, logout_view

urlpatterns = [
    
    path("", home_view, name = "home"),
    path("bookingpsico/login", login_view, name = "login"),
    path("bookingpsico/crear_reserva/", crear_reserva, name = "crear_reserva"),
    path("bookingpsico/todas_las_reservas/", todas_las_reservas, name = "todas_las_reservas"),
    path("bookingpsico/terapias/", terapias_view, name = "terapias"),
    path("bookingpsico/terapeutas", terapeutas, name = "terapeutas"),
    path("bookingpsico/detail_view", detail_view, name = "detail_view"),
    path("bookingpsico/buscar/", search_view, name = "buscar_reservas"),
    path("bookingpsico/register/", register, name = "registro"),
    path("bookingpsico/logout/", logout_view, name = "logout"),
]
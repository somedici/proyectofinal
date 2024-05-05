from django.urls import path
from django.http import HttpResponse

from .views import home_view, crear_reserva, terapeutas,login_view, terapias_view, detail_view, search_view, todas_las_reservas, register, logout_view, about, redirect_to_login, contact, editar_reserva

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name= 'home_view'),
    path('bookingpsico/', views.home_view, name='home'),
    path('bookingpsico/login/', views.login_view, name='login'),
    path('bookingpsico/crear_reserva/', views.crear_reserva, name='crear_reserva'),
    path('bookingpsico/todas_las_reservas/', views.todas_las_reservas, name='todas_las_reservas'),
    path('bookingpsico/terapias/', views.terapias_view, name='terapias'),
    path('bookingpsico/terapeutas/', views.terapeutas, name='terapeutas'),
    path('bookingpsico/detail_view/', views.detail_view, name='detail_view'),
    path('bookingpsico/buscar/', views.search_view, name='buscar_terapeuta'),
    path('bookingpsico/register/', views.register, name='registro'),
    path('bookingpsico/logout/', views.logout_view, name='logout'),
    path('bookingpsico/about/', views.about, name='about'),
    path('bookingpsico/contact/', views.contact, name='contacta'),
    path('bookingpsico/editar_reserva/<int:reserva_id>/', views.editar_reserva, name='editar_reserva'),
]

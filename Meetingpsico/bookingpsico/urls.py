from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def mi_vista(xx):
    return HttpResponse("<h2>Encuentra tu camino hacia el bienestar<h1>") 

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", mi_vista),
    path("bookingpsico/", include("bookingpsico.urls")),
]
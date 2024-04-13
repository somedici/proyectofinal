from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('booking/', include('bookingpsico.urls')),  # Incluye el módulo de URLs de bookingpsico
] 

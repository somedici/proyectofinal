from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('bookingpsico/', include('bookingpsico.urls')),  # Incluye el módulo de URLs de bookingpsico
    path('', include('bookingpsico.urls')),  # Asegúrate de reemplazar 'nombre_de_tu_aplicacion'
]


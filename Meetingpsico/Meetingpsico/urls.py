from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('bookingpsico/', include('bookingpsico.urls')), 
    path('', include('bookingpsico.urls')),  
]


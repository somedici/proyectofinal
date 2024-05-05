from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class Reserva(models.Model):
    usuario = models.CharField(max_length=100)
    fecha = models.DateField()
    hora = models.TimeField()
    tipo_terapia = models.CharField(max_length=100)
    terapeuta = models.ForeignKey('Terapeuta', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.usuario} - {self.hora} - {self.fecha} - {self.tipo_terapia} {self.terapeuta} "

class Terapeuta(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class Terapia(models.Model):
    nombre = models.CharField(max_length=100)
    def __str___(self):
        return self.nombre
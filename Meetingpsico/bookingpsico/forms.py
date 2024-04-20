from django import forms
from .models import Reserva, Sala


class Reserva(forms.Form):
    nombre= forms.CharField(max_length=50, required=True, label="Ingresar nombre de usuario")
    correo_electrónico = forms.CharField(max_length=50, required=True, label="Ingresar tu correo electrónico")

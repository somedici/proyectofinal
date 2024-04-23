from django import forms
from .models import Reserva, Terapeuta

class ReservaCreateForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ["nombre_usuario",
                  "fecha", 
                  "hora", 
                  "tipo_terapia", 
                  "terapeuta"]

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

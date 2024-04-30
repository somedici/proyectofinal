from django import forms
from .models import Reserva, Terapeuta
from django.contrib.auth.models import User

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

class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(label='Correo electrónico', max_length=254, help_text='Ingrese su dirección de correo electrónico')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
        help_texts = {k: "" for k in fields}  


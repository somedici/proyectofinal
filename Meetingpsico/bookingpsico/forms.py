from django import forms

from .models import Reserva, Sala


class ReservaSearchForm(forms.Form):
    nombre_de_usuario = forms.CharField(max_length=50, required=True, label="Ingresar nombre de usuario")

class ReservaCreateForm(forms.Form):
    pass

class SalaCreateForm(forms.ModelForm):
    class Meta:
        model = Sala
        fields = ['nombre', 'disponibilidad_de_terapeuta', 'terapia']
        labels = {
            'nombre': 'Elegir un nombre para la Sala',
            'disponibilidad_de_terapeuta': "Disponible",
            'terapia': '',
                    
        }

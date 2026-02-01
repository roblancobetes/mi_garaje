from django import forms
from .models import Coche

class formularioNuevoCoche(forms.Form):
    marca = forms.CharField(max_length=80)
    modelo = forms.CharField(max_length=80)
    dueno = forms.CharField(max_length=120)  # simple: nombre del dueño
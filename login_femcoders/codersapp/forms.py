from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, EmailInput
from django import forms

from .models import *

class EvaluacionForm(ModelForm):
    class Meta:
        model = Evaluacion
        fields = [
                    'nota',
                    'comentario',
                        ]
        labels = {
            'nota': 'Nota',
            'comentario':'Comentario',

        }

class AlumnoForm(ModelForm):
    class Meta:
        model = Alumno
        fields = '__all__'
        labels = {
            'nombre': 'Nombre',
            'apellido':'Apellidos',
            'dni': 'DNI',
            'telefono': 'Teléfono',
            'email': 'Email',
            'materia': 'Materia',
            'fNacimiento': 'F.Nacimiento',


        }

class NuevaEvaluacionForm(ModelForm):
    class Meta:
        model = Evaluacion
        fields = '__all__'
        labels = {
            'materia': 'Materia',
            'alumno': 'Alumno',
            'nota': 'Nota',
            'comentario':'Comentario',

        }

class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
                'username',
                'first_name',
                'last_name',
                'email',
                   ]
        labels = {
            'username':'Nombre de usuario',
            'first_name':'Nombre',
            'last_name':'Apellidos',
            'email':'Correo',

        }

        widgets = {
            'email': EmailInput(attrs={'type':'email'})
        }

class ImagenForm(forms.ModelForm):

    materia = forms.ModelMultipleChoiceField(queryset=Materia.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Alumno
        fields = '__all__'
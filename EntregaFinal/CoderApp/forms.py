from django import forms
from dataclasses import fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class PlantaFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    nombreCientifico = forms.CharField(max_length=40)
    deInterior = forms.CharField(max_length=40)

class ArbolFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    nombreCientifico = forms.CharField(max_length=40)
    alturaMax = forms.IntegerField()

class CactusFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    nombreCientifico = forms.CharField(max_length=40)
    diasSinAgua = forms.IntegerField()

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label= 'Contraseña', widget= forms.PasswordInput)
    password2 = forms.CharField(label= 'repite la contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        print(model)
        fields = ['username', 'password1', 'password2']
        help_texts= {c:"" for c in fields}
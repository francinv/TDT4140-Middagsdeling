from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    name = forms.CharField(label='Fullt navn')
    allergies = forms.CharField(label='Allergier')
    address = forms.CharField(label='Gatenavn og husnummer')
    postnr = forms.IntegerField(label='Postnummer')
    poststed = forms.CharField(label='Sted')

    class Meta:
        model = User
        fields = ['username', 'name', 'allergies', 'address', 'postnr', 'poststed', 'password1', 'password2']

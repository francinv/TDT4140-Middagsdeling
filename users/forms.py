from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    name = forms.CharField(label='Fullt navn')
    ALLERGIES_CHOICES=[
        ('gluten', 'Gluten'),
        ('laktose', 'Laktose'),
        ('egg', 'Egg'),
        ('nøtter', 'Nøtter'),
        ('ingen', 'Ingen'),
    ]
    allergies = forms.MultipleChoiceField(
        required=True,
        widget=forms.CheckboxSelectMultiple,
        choices=ALLERGIES_CHOICES
    )
    address = forms.CharField(label='Gatenavn og husnummer')
    postnr = forms.IntegerField(label='Postnummer')
    poststed = forms.CharField(label='Sted')

    class Meta:
        model = User
        fields = ['username', 'name', 'allergies', 'address', 'postnr', 'poststed', 'password1', 'password2']

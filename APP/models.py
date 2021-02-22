from django.db import models
from django.forms import forms
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models

class Middag(models.Model):
    title = models.CharField(max_length=125)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    guests = models.IntegerField()
    YES = 'Y'
    NO = 'N'
    GLUTEN = 'GL'
    LAKTOSE = 'LA'
    EGG = 'EG'
    NØTTER = 'NØ'
    sharing_choices = [
        (YES, 'Ja'),
        (NO, 'Nei'),
    ]
    sharing = models.CharField(
        max_length=2,
        choices=sharing_choices,
        default=YES,
    )
    allergener_choices =[
        (GLUTEN, 'Gluten'),
        (LAKTOSE, 'Laktose'),
        (EGG, 'Egg'),
        (NØTTER, 'Nøtter'),
    ]
    allergener = models.CharField(
        max_length=2,
        choices=allergener_choices,
        default=None
    )

    def __str__(self):
        return self.title


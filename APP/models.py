from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from multiselectfield import MultiSelectField

sharing_choices = [
        ('ja', 'Ja'),
        ('no', 'Nei'),
]
allergener_choices =[
        ('GLUTEN', 'Gluten'),
        ('LAKTOSE', 'Laktose'),
        ('EGG', 'Egg'),
        ('NØTTER', 'Nøtter'),
        ('INGEN', 'Ingen'),
]

class Middag(models.Model):
    title = models.CharField(max_length=125)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    guests = models.PositiveSmallIntegerField()
    sharing = models.CharField(
        max_length=2,
        choices=sharing_choices,
        default='ja',
    )
    sharing_cost = models.PositiveSmallIntegerField()
    allergener = MultiSelectField(choices=allergener_choices)
    address = models.CharField(max_length=200, default=None)
    postnr = models.PositiveSmallIntegerField(default=None)
    poststed = models.CharField(max_length=200, default=None)
    date_of_dinner = models.DateTimeField(default=None)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('middag-detail', kwargs={'pk': self.pk})

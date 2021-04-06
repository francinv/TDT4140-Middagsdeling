from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

from APP.models import Middag
from multiselectfield import MultiSelectField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Profile'


class Message(models.Model):
    User = settings.AUTH_USER_MODEL
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    to_user = models.ForeignKey(User, related_name='receiver', on_delete=models.CASCADE)
    message = models.TextField()







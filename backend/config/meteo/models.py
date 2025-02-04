from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):...

class City(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    count = models.IntegerField()
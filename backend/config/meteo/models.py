from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):...

class City(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    longitude = models.CharField(max_length=100, default='0')
    latitude = models.CharField(max_length=100, default='0')
    count_city = models.IntegerField()

    def __str__(self):
        return self.name
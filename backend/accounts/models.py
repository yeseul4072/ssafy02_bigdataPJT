from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.core.validators import MinValueValidator


# Create your models here.
class User(AbstractUser):
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    nickname = models.CharField(max_length=50)
    is_director = models.BooleanField(default=False)
    kindergarten_id = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(0)])
    profile_image = models.ImageField(upload_to="profile/%Y/%m/%d", null=True)

class Child(models.Model):
    age = models.IntegerField()
    gender = models.CharField(max_length=1)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

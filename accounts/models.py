from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    realname = models.CharField(max_length=4, blank=False)
    nickname = models.CharField(max_length=10, blank=False)

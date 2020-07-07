
from django.db import models
from django.contrib.auth.models import User


class Shortener(models.Model):
    uid         = models.AutoField(primary_key=True)
    slug        = models.CharField(max_length=11, unique=True)
    requestURL  = models.CharField(max_length=1000, unique=True)
    responseURL = models.CharField(max_length=100, unique=True)
    date        = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.requestURL


from cgitb import text
from contextlib import nullcontext
from datetime import date
from email.mime import image
from unicodedata import name
from unittest.util import _MAX_LENGTH
from django.db import models


class Reservation(models.Model):
    name = models.CharField(max_length=24)

    def __str__(self):
        return self.name


class PrizeWinners(models.Model):
    winner= models.CharField(max_length=200, null=True)
    text= models.TextField(null=True)
    pub_date = models.DateField(null=True)
    prize= models.CharField(max_length=200, null=True)
    image= models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.prize

    
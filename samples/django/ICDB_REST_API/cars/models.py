"""
Models for the cars app.
"""
from django.db import models


class Car(models.Model):
    """A car."""
    make = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    year = models.IntegerField()

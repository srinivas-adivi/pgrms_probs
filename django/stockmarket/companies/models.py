"""
Models for the companies app.
"""
from django.db import models
from decimal import Decimal


class Company(models.Model):
    """A company."""
    code = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=255)
    group = models.CharField(max_length=255)
    type = models.CharField(max_length=10)


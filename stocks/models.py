"""
Models for the stocks app.
"""
from django.db import models
from decimal import Decimal
from companies.models import Company


class Stock(models.Model):
    """A stock."""
    date = models.DateField()
    opening_price = models.DecimalField(max_digits=10, decimal_places=2)
    closing_price = models.DecimalField(max_digits=10, decimal_places=2)
    company = models.ForeignKey(Company)
    #, related_name="stock_and_company")
    
    class Meta:
        unique_together = ("date", "company")


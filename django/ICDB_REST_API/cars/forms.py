"""
Forms for the cars app.
"""
from django import forms
from cars.models import Car


class CarForm(forms.ModelForm):
    """Form for the Car model."""
    class Meta:
        model = Car

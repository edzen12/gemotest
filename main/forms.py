from django import forms
from django.forms import fields
from main.models import Gemotest


class GemotestForm(forms.Form):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    surname = forms.CharField(max_length=255)
    number_of_phone = forms.CharField(max_length=255)
    date_of_birth = forms.DateField()
    email = forms.EmailField()
    number_of_passport = forms.CharField(max_length=255)
    address = forms.CharField(max_length=255)
    date_of_give_bio = forms.DateTimeField()
    date_completed = forms.DateTimeField()
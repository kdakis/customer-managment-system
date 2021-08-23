from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model
from django.forms import fields
from .models import Customer

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}



class CustomerModelForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = (
            'name',
            'surname',
            'ssn',
            'phone',
            'city',
            'district'
        )


class CustomerForm(forms.Form):

    name = forms.CharField()
    surname = forms.CharField()
    ssn = forms.CharField()
    phone = forms.CharField()
    city = forms.CharField()
    district = forms.CharField()
    
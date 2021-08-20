from django import forms
from django.forms import fields
from .models import Customer

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
    
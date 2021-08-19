from django import forms


class CustomerForm(forms.Form):

    name = forms.CharField()
    surname = forms.CharField()
    ssn = forms.CharField()
    phone = forms.CharField()
    city = forms.CharField()
    district = forms.CharField()
    
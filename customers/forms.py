from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model
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

    def clean(self):
        cleaned_data = super().clean()
        ssn = cleaned_data.get("ssn")
        phone = cleaned_data.get("phone")
        if phone and ssn:
            if (len(phone) != 10 or len(ssn) != 11):
                if (len(phone) != 10):
                    raise forms.ValidationError(
                        "Please check your phone number!!"
                        )
                if (len(ssn) != 11):
                    raise forms.ValidationError(
                        "Please check your ssn!!"
                        )
            else:
                return cleaned_data
        else:
            return None

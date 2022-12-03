from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UsernameField

Customer = get_user_model()


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('username', 'first_name', 
            'last_name','email')
        field_classes = {"username": UsernameField}

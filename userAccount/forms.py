from django import forms
from django.forms import CharField, PasswordInput
from django.forms import ModelForm


from .import forms

from custom_user_model.models import User

class UserRgistrationForm(forms.ModelForm):
    password =forms.CharField(widget=forms.PasswordInput())
    confrim_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model=User
        fields=['first_name','last_name','username','email','phone','password']



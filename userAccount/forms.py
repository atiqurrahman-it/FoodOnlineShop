from django import forms
from django.forms import CharField, PasswordInput
from django.forms import ModelForm


from .import forms
from django.forms import ValidationError

from custom_user_model.models import User

class UserRgistrationForm(forms.ModelForm):
    password =forms.CharField(widget=forms.PasswordInput())
    confrim_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model=User
        fields=['first_name','last_name','username','email','phone','password']

    def clean(self):
        cleaned_data=super(UserRgistrationForm,self).clean()
        password=cleaned_data.get('password')
        confrim_password=cleaned_data.get('confrim_password')

        if password != confrim_password:
            raise forms.ValidationError("password not match ")
        



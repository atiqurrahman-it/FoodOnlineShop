from django import forms
from django.forms import CharField, PasswordInput,FileField,FileInput
from django.forms import ModelForm

# validataion error 
from .validators import allow_only_images_validator

from .import forms
from django.forms import ValidationError

from custom_user_model.models import User

from .models import UserProfile

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

#allow_only_images_validator import validators.py 
class UserPrifileForm(forms.ModelForm):
    profile_picture = forms.FileField(widget=forms.FileInput(attrs={'class': 'btn btn-info'}),validators=[allow_only_images_validator])
    cover_picture = forms.FileField(widget=forms.FileInput(attrs={'class': 'btn btn-info'}),validators=[allow_only_images_validator])

    class Meta:
        model=UserProfile
        fields=['profile_picture','cover_picture','address_line1','address_line2','country','state','city','pin_code','latitude','longitude']
    

        



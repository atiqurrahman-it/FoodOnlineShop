from custom_user_model.models import User
from django import forms
from django.forms import (CharField, FileField, FileInput, ModelForm,
                          PasswordInput, TextInput, ValidationError)

from . import forms
from .models import UserProfile
# validataion error 
from .validators import allow_only_images_validator


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
    address=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'start typing ..','required': "required"},))
    profile_picture = forms.FileField(widget=forms.FileInput(attrs={'class': 'btn btn-info'}),validators=[allow_only_images_validator])
    cover_picture = forms.FileField(widget=forms.FileInput(attrs={'class': 'btn btn-info'}),validators=[allow_only_images_validator])

    # just read only not edit this cloum 
    # latitude=forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    # longitude=forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))

    class Meta:
        model=UserProfile
        fields=['profile_picture','cover_picture','address','country','state','city','pin_code','latitude','longitude']
       

    # just read only not edit this cloum 
    # ek vabe korle hobe ...ei khane opor er niyome korchi line 33
    def __init__(self, *args, **kwargs):
        super(UserPrifileForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if field=='latitude' or  field=='longitude':
                self.fields[field].widget.attrs['readonly'] = 'readonly'

        





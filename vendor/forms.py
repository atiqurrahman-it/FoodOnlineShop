from django import forms

from .models import Vendor

# validataion error 
from userAccount.validators import allow_only_images_validator

class vendorForm(forms.ModelForm):
    vedor_license = forms.FileField(widget=forms.FileInput(attrs={'class': 'btn btn-info'}),validators=[allow_only_images_validator])
    class Meta:
        model = Vendor
        fields = ("vendor_name","vedor_license",)

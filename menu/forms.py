from distutils.text_file import TextFile
from django import forms

from userAccount.validators import allow_only_images_validator
from .models import Category, FoodItem



class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        # vendor field ta view file auto add hobe ..user add korte parbe na 
        fields = ['category_name', 'description']


class FoodItemForm(forms.ModelForm):
    image = forms.FileField(widget=forms.FileInput(attrs={'class': 'btn btn-info w-100'}), validators=[allow_only_images_validator])
    description= forms.CharField(widget=forms.Textarea(attrs={'rows':3,'cols':5}))
    # forms.CharField(widget=forms.Textarea(attrs={'rows':30}))
    class Meta:
        model = FoodItem
        # vendor field ta view file auto add hobe ..user add korte parbe na 
        fields = ['food_title','category', 'description', 'price', 'image', 'is_available']
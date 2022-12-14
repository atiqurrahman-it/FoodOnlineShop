from django.db import models
# Create your models here.
from custom_user_model.models import User




class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,blank=True,null=True)
    profile_picture=models.ImageField(upload_to='user/profile_pictuer',blank=True,null=True)
    cover_picture=models.ImageField(upload_to='user/cover_picture',blank=True,null=True)
    address=models.CharField(max_length=200, blank=True,null=True)
    country=models.CharField(max_length=30,blank=True,null=True)
    state=models.CharField(max_length=20,blank=True,null=True)
    city=models.CharField(max_length=20,blank=True,null=True)
    pin_code=models.CharField(max_length=8,blank=True,null=True)
    # Latitude and Longitude are the units that represent the coordinates at geographic coordinate system. 
    # To make a search, use the name of a place, city, state, or address, or click the location on the map to find lat long coordinates.
    latitude=models.CharField(max_length=20,blank=True,null=True)
    longitude=models.CharField(max_length=20,blank=True,null=True)
    create_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now_add=True)

    # def full_adderss(self):
    #     return f'{self.address_line1},{self.address_line2}'


    def __str__(self):
        return self.user.email



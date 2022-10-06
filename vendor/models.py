from distutils.command.upload import upload
from tkinter import CASCADE
from django.db import models

# Create your models here.
from custom_user_model.models import User
from userAccount.models import UserProfile



class Vendor(models.Model):
    user=models.OneToOneField(User,related_name="user",on_delete=models.CASCADE)
    user_profil=models.OneToOneField(UserProfile,related_name="userprofile",on_delete=models.CASCADE)
    vendor_name=models.CharField(max_length=50)
    vedor_license=models.ImageField(upload_to='vendor/license')
    is_approved=models.BooleanField(default=False)
    create_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.vendor_name


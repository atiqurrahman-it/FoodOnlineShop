from distutils.command.upload import upload
from tkinter import CASCADE

# Create your models here.
from custom_user_model.models import User
from django.db import models
from userAccount.email_varification import send_notification
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


    #  admin panel theke vendor er  save button e click korle then run hobe  
    def save(self, *args, **kwargs):
        if self.pk is not None:
            # Update
            orig = Vendor.objects.get(pk=self.pk)
            if orig.is_approved != self.is_approved:
                mail_template = 'useraccounts/emails/admin_approval_email.html'
                context = {
                    'user': self.user,
                    'is_approved': self.is_approved,
                    'to_email': self.user.email,
                }
            
                if self.is_approved == True:
                    # Send notification email 
                    # admin approve korle vendor er  kache email jabe 
                    mail_subject = "Congratulations! Your restaurant has been approved."
                    send_notification(mail_subject, mail_template, context)

                else:
                    # Send notification email
                    mail_subject = "We're sorry! You are not eligible for publishing your food menu on our marketplace."
                    send_notification(mail_subject, mail_template, context)

        return super(Vendor, self).save(*args, **kwargs)



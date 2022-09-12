from custom_user_model.models import User
from userAccount.models import UserProfile


# cuto create usr profile  start 
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
# cuto create usr profile  End 


# auto create user profile  when create user 

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    # instance meens current user (je user create korbo or update korbo)
    # create meens user create korle True .... and user update korle Flase return  korbe 

    # user profile crete hobe user create korle 
    if created:
        # print(created)  create ture or flase return kore .....
        print("create userprofile")
        UserProfile.objects.create(user=instance)
    # user edit korle user profile update hobe
    else:
        try:
            print("profile update ")
            user_profile_update= UserProfile.objects.get(user=instance)
            user_profile_update.save()
            # create userprofile is not exist
            #jodi user theke but userprofile delete kora hoiye thele tahole abar userprofile create korbe 
        except:
            UserProfile.objects.create(user=instance)


@receiver(pre_save, sender=User)
def pre_save_profile_receiver(sender, instance, **kwargs):
    pass

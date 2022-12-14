from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils import timezone

# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email, username,first_name,last_name, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have an username ')
        
        #unique username check kra bad ache 

        # normalize_email meens currect provide email. like  email upper case letter convert lower case 
        email=self.normalize_email(email)
        # user name use na korle create_user and superusr e use kortam na 
        user = self.model(
            email=email,username=username,
            first_name=first_name,last_name=last_name,
         )
        #  set_password  meens password encode korbe ......
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username,email,first_name,last_name, password=None):
        email=self.normalize_email(email)

        user=self.create_user(
            username=username,email=email,
            first_name=first_name,last_name=last_name,
            password=password,
        )
        user.is_admin = True
        user.is_superuser=True
        user.is_staff=True
        user.is_active=True
        user.save(using=self._db)
        return user
       


class User(AbstractBaseUser):
    Vendor=1
    CUSTOMER=2
    ROLE_CHOICE=(
        (Vendor,'Vendor'),
        (CUSTOMER,'Customer'),
    )
    # user= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    username=models.CharField(max_length=50,unique=True,blank=True)
    email = models.EmailField(verbose_name='email address', max_length=255,unique=True,)
    date_of_birth = models.DateField(blank=True,null=True)
    phone=models.IntegerField(blank=True,null=True)
    role=models.PositiveSmallIntegerField(choices=ROLE_CHOICE,null=True,blank=True)
     # required fields
    date_joined= models.DateTimeField(default=timezone.now)
    last_login=models.DateTimeField(default=timezone.now)
    create_date=models.DateTimeField(default=timezone.now)
    modified_date=models.DateTimeField(auto_now=True)

    is_admin=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)


    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name']
    
    
     # optional
    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    # dashboard e login e jonno customer or vendor
    def get_role(self):
        if self.role==1:
            userrole="Vendor"
            
        elif self.role==2:
            userrole="customer"
            
        # problem show hobe role emty thakle 
        # return userrole

        try:
            return userrole
        except:
            print("An exception occurred")
      
        
        
       






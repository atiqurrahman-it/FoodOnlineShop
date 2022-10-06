from ast import Pass
from urllib import request
from wsgiref.util import request_uri
from xml.dom import ValidationErr
# detect usrl file path 
from .userdetect import detectUser

from custom_user_model.models import User
#message show 
from django.contrib import messages
# login 
from django.contrib.auth import authenticate, login, logout 
from django.http import HttpResponse
from django.shortcuts import redirect, render
from vendor.forms import vendorForm

from userAccount.models import UserProfile

from .forms import UserRgistrationForm

from django.contrib.auth.decorators import login_required,user_passes_test
from django.core.exceptions import PermissionDenied

#verify customer vs vender deashboard 

def check_role_venders(user):
    if user.role==1:
        return True
    else:
        raise PermissionDenied
def check_role_customer(user):
    if user.role==2:
        return True
    else:
        raise PermissionDenied




# Create your views here.
def RegisterUser(request):
     # if already registerUser 
    if request.user.is_authenticated:
        messages.warning(request, 'You are already registerUser !')
        return redirect('myaccount')
    elif request.method == 'POST':
        form=UserRgistrationForm(request.POST)
        if form.is_valid():
            # create the user using from  start (problem 
            #Invalid password format or unknown hashing algorithm.)
            # user=form.save(commit=False) #commit=false meens save er jonno ready but save hobe na .....
            # user.role=User.CUSTOMER
            # user.save() #defule role customer add korlam
            # end 
            #create the user using creatre_user method
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            confrim_password=form.cleaned_data['confrim_password']
            # password mach check  ai khane korte partam 
            # mach check korchi singnal.py file e 
            # mach check korchi singnal.py file e 
            if password==confrim_password:
                print("password mach")
            else:
                print("password not match")
                
            user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
            user.role=User.CUSTOMER
            user.save() #defule role customer add korlam
            messages.error(request, 'your account has been registerd successfully')
            return redirect('login')
        else:
            print("invalid")
            print(form.errors)


        
    else:
        form=UserRgistrationForm()
    data={
        'form':form,
    }  
    return render(request,'useraccounts/registration.html',data)





def RegistrationVendor(request):
         # if already registerUser 
    if request.user.is_authenticated:
        messages.warning(request, 'You are already registerVendor !')
        return redirect('myaccount')
    elif request.method=="POST":
        form=UserRgistrationForm(request.POST)
        v_form=vendorForm(request.POST,request.FILES)
        # both form valid then save model 
        if form.is_valid() and  v_form.is_valid() :
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
            user.role=User.Vendor
            user.save() #defule role Vendor add korlam

            vendor=v_form.save(commit=False)
            vendor.user=user
            Userprofile=UserProfile.objects.get(user=user)
            vendor.user_profil=Userprofile
            vendor.save()
            messages.error(request, 'your account has been registerd successfully')
          
            
        else:
            print("Invalid Form ")
            print(form.error)
            
    else:
        form=UserRgistrationForm()
        v_form=vendorForm()

    data={
        "form":form,
        "v_form":v_form
    }
    return render(request,'useraccounts/registrationvedor.html',data)



def Login(request):
    # if already login 
    if request.user.is_authenticated:
        messages.warning(request, 'You are already logged in!')
        return redirect('myaccount')
    elif request.method=='POST':
        
        email=request.POST['email']
        password=request.POST['password']

        user = authenticate(request, email=email, password=password)
        # is_activate is ture then login 
        if user is not None:
            login(request, user)
            messages.error(request, 'successfully login ....select your favorite  food  !')
            return redirect('myaccount')
        # Redirect to a success page.
        else:
            print("user is not found ")
            messages.error(request, 'email or password not match . please try again !')
            return redirect('login')
            
    return render(request,'useraccounts/login.html')

def Logout(request):
    logout(request)
    messages.error(request, 'successfully login out  !')
    return redirect('login')

@login_required(login_url='login')
def Myaccount(request):
    user=request.user
    redirectUrl=detectUser(user)
    return redirect(redirectUrl)


@login_required(login_url='login')
@user_passes_test(check_role_venders)
def VenderDashbord(request):
    return render(request,'useraccounts/vendashboard.html')


@login_required(login_url='login')
@user_passes_test(check_role_customer)
def CousDashbord(request):
    return render(request,'useraccounts/cousdashboard.html')


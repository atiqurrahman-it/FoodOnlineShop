
from re import U
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

#email varification 
from django.contrib.auth.tokens import default_token_generator
from django.http import Http404
from django.utils.http import urlsafe_base64_decode


from .email_varification import send_varification_email


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
            user.save() # efule role customer add korlam

            # Email Varification 
            # send_varification_email this is my create def email_varification.py 
            mail_subject = 'Please activate your account'
            email_template = 'useraccounts/emails/email_vaification.html'
            send_varification_email(request, user,mail_subject,email_template)

            messages.error(request, 'your account has been registerd successfully. Send code your email')
            return redirect('registrationUser')
        else:
            print("invalid")
            print(form.errors)


        
    else:
        form=UserRgistrationForm()
    data={
        'form':form,
    }  
    return render(request,'useraccounts/registration.html',data)


# Email  varificatin active view 
def activate(request,uid,token):
    try:
        uid=urlsafe_base64_decode(uid).decode()
        user = User.objects.get(pk=uid)
    except:
        raise Http404("No user found ")
    if user is not None and default_token_generator.check_token(user,token):
        user.is_active = True
        user.save()
        messages.error(request, 'congratulation your account is activated ')
        return redirect('homepage')
    else:
        return HttpResponse('Activation link is invalid!')




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
            # print(form.error)
            
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


# forgot password 
# send_varification_email def import kora hoiche 

def Forgot_password(request):
    if request.POST:
        email=request.POST['email']
        # if email exisits then conditon ture
        if User.objects.filter(email=email).exists():
            # user find out 
            user=User.objects.get(email__exact=email)
            # send reset  password email 
            mail_subject = 'Reset Your password '
            email_template = 'useraccounts/emails/reset_password_email.html'
            send_varification_email(request, user,mail_subject,email_template) 

            messages.error(request, 'password reset link has been  send your email !')
            return redirect('login')
        else:
            messages.error(request, 'Account does not exists  !')
            return redirect('forgot_password')

    return render(request,'useraccounts/forgot_password.html')


def reset_password_validate(request,uid,token):
    try:
        uid=urlsafe_base64_decode(uid).decode()
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
        raise Http404("No user found ")

    if user is not None and default_token_generator.check_token(user,token):
        request.session['uid'] = uid
        messages.info(request, 'Please reset your password')
        return redirect('reset_password')
      
    else:
        messages.error(request,'This link has been exprired')
        return redirect('myaccount')



def Reset_password(request):
    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            pk = request.session.get('uid')
            user = User.objects.get(pk=pk)
            user.set_password(password)
            user.is_active = True
            user.save()
            messages.success(request, 'Password reset successful')
            return redirect('login')
        else:
            messages.error(request, 'Password do not match!')
            return redirect('reset_password')
    return render(request, 'useraccounts/reset_password.html')

# end forgot password 
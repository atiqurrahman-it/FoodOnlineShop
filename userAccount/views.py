from ast import Pass
from xml.dom import ValidationErr
from django.shortcuts import render,redirect
from django.http import HttpResponse

from .forms import UserRgistrationForm
from vendor.forms import vendorForm
from custom_user_model.models import User

#message show 
from django.contrib import messages

# Create your views here.
def Register(request):
    if request.method == 'POST':
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
            if password==confrim_password:
                print("password mach")
            else:
                print("password not match")
                
            user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
            user.role=User.CUSTOMER
            user.save() #defule role customer add korlam
            messages.success(request, ' successfully login ')
            return redirect('registrationUser')
        else:
            print("invalid")
            print(form.errors)


        
    else:
        form=UserRgistrationForm()
    data={
        'form':form,
    }  
    return render(request,'single_page/registration.html',data)





def RegistrationVendor(request):
    if request.method=="POST":
        form=UserRgistrationForm(request.POST)
        v_form=vendorForm(request.POST,request.FILES)\
        # both form valid then save model 
        if form.is_valid() and  v_form.is_valid() :
            print(form)
            print(v_form)
            
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
    return render(request,'single_page/registrationvedor.html',data)
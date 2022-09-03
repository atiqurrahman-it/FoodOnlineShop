from django.shortcuts import render,redirect
from django.http import HttpResponse

from .forms import UserRgistrationForm
from custom_user_model.models import User

# Create your views here.

def Register(request):
    if request.method == 'POST':
        print(request.POST)
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
            user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
            user.role=User.CUSTOMER
            user.save() #defule role customer add korlam

            return redirect('register')
        return HttpResponse("Form is not  valid")

        
    else:
        form=UserRgistrationForm()
    data={
        'form':form,
    }  
    return render(request,'single_page/registration.html',data)

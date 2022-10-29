# Create your views here.
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import get_object_or_404, redirect, render
# import from
from userAccount.forms import UserPrifileForm
from userAccount.models import UserProfile
from userAccount.views import check_role_venders

from vendor.forms import vendorForm
from menu.forms import CategoryForm
# import model 
from vendor.models import Vendor
from menu.models import Category,FoodItem


@login_required(login_url='login')
@user_passes_test(check_role_venders)
def Vprifile(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    vendor = get_object_or_404(Vendor, user=request.user)

    if request.method == 'POST':
        profile_form = UserPrifileForm(request.POST, request.FILES, instance=profile)
        vendor_form = vendorForm(request.POST, request.FILES, instance=vendor)
        if profile_form.is_valid() and vendor_form.is_valid():
            profile_form.save()
            vendor_form.save()
            messages.success(request, 'Settings updated.')
            return redirect('vprofile')
        else:
            print(profile_form.errors)
            print(vendor_form.errors)
    else:
        profile_form = UserPrifileForm(instance=profile)
        vendor_form=vendorForm(instance=vendor)

    data={
        "profile_form":profile_form,
        "vendor_form":vendor_form,
        "profile":profile,
        "vendor":vendor,
    }
  

    return render(request,'vendor/profile.html',data)
#common query gula function moddome likhte pari
# same query repited korte na hoi

def get_vendor(request):
    vendor=Vendor.objects.get(user=request.user)
    return vendor


def menue_builder(request):
    #individual category show 
    try:
        vendor=get_vendor(request) # import line 49
        category=Category.objects.filter(vendor=vendor)
    except:
        user:None

  
    data={
        "categories":category,
    }
    return render(request,'vendor/menue_builder.html',data)


def FoodItemByCategory(request,id):
    vendor=get_vendor(request)
    category=get_object_or_404(Category,pk=id)
    fooditems=FoodItem.objects.filter(category=category,vendor=vendor)
    print(fooditems)
    data={
        "fooditems":fooditems,
        "category":category,
    }

    return render(request,'vendor/fooditems_by_category.html',data)

def add_category(request):
    form=CategoryForm()
    data={
        "form":form,
    }
    return render(request,'vendor/add_category.html',data)


    

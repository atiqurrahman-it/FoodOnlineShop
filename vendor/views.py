# Create your views here.
from tkinter.messagebox import NO
from webbrowser import get
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import get_object_or_404, redirect, render
from django.template.defaultfilters import slugify

# import from
from userAccount.forms import UserPrifileForm
from userAccount.models import UserProfile
from userAccount.views import check_role_venders

from vendor.forms import vendorForm
from menu.forms import CategoryForm,FoodItemForm
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


@login_required(login_url='login')
@user_passes_test(check_role_venders)
def menue_builder(request):
    #individual category show 
    try:
        vendor=get_vendor(request) # import line 54
        category=Category.objects.filter(vendor=vendor).order_by('created_at')
    except:
        user:None

  
    data={
        "categories":category,
    }
    return render(request,'vendor/menue_builder.html',data)


@login_required(login_url='login')
@user_passes_test(check_role_venders)
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


#Category  CURD Start  

@login_required(login_url='login')
@user_passes_test(check_role_venders)
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.vendor = get_vendor(request) # user auto add
            category.save() # create user name then id create 

            # from django.template.defaultfilters import slugify
            category_name = form.cleaned_data['category_name']
            category.slug = slugify(category_name)+'-'+str(category.pk) # chicken-15

            category.save()
            messages.success(request, 'category added successfully !')
            return redirect('menue_builder')
        else:
            print(form.errors)

    else:
        form=CategoryForm()
    data={
        "form":form,
    }
    return render(request,'vendor/add_category.html',data)


@login_required(login_url='login')
@user_passes_test(check_role_venders)
def edit_category(request,id):
    category = get_object_or_404(Category, pk=id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            category = form.save(commit=False)

            # from django.template.defaultfilters import slugify
            category_name = form.cleaned_data['category_name']
            category.vendor = get_vendor(request)
            category.slug = slugify(category_name)

            category.save()
            messages.success(request, 'Category updated successfully!')
            return redirect('menue_builder')
            
        else:
            print(form.errors)
    else:
        form = CategoryForm(instance=category)

    context = {
        'form': form,
        'category': category,
    }
    return render(request, 'vendor/edit_category.html', context)



@login_required(login_url='login')
@user_passes_test(check_role_venders)
def delete_category(request,id=None):
    category = get_object_or_404(Category, pk=id)
    category.delete()
    messages.success(request, 'Category has been deleted successfully!')
    return redirect('menue_builder')
#Category  CURD End 


#FoodItem CURD start 

@login_required(login_url='login')
@user_passes_test(check_role_venders)
def add_food(request):
    if request.method == 'POST':
        form = FoodItemForm(request.POST,request.FILES)
        if form.is_valid():
            foodtitle = form.cleaned_data['food_title']
            food=form.save(commit=False)
            food.vendor = get_vendor(request)
            food.slug = slugify(foodtitle)
            food.save()
            messages.success(request, 'Food Item added successfully!')

            # je category save hobe oi vatergory page e redirect hobe 
            return redirect('FoodItemByCategory',food.category.id)
            
        else:
            print(form.errors)
    else: 
         form =FoodItemForm()
         # add food er somoy jeno all user er category show na kore 
         # je login thakbe sudu or category show korbe 
         # FoodItem import menu app theke
         # get_vendor() import 54 line 
         form.fields['category'].queryset=Category.objects.filter(vendor=get_vendor(request))

    data={
        "form":form,
    }
    return render(request, 'vendor/add_fooditem.html', data)

@login_required(login_url='login')
@user_passes_test(check_role_venders)
def edit_food(request,id=None):
    fooditem=get_object_or_404(FoodItem,pk=id)
    if request.method == 'POST':
        form = FoodItemForm(request.POST,request.FILES,instance=fooditem)
        if form.is_valid():
            foodtitle = form.cleaned_data['food_title']
            food=form.save(commit=False)
            food.vendor = get_vendor(request)
            food.slug = slugify(foodtitle)
            food.save()
            messages.success(request, 'Food Items updated successfully!')
            return redirect('FoodItemByCategory',food.category.id)


        else:
            print(form.errors)
    else:
        form = FoodItemForm(instance=fooditem)
         # add food er somoy jeno all user er category show na kore 
         # je login thakbe sudu or category show korbe 
         # FoodItem import menu app theke
         # get_vendor() import 54 line 
        form.fields['category'].queryset=Category.objects.filter(vendor=get_vendor(request))

    data={
        "form":form,
        "fooditem":fooditem,
    }
    return render(request, 'vendor/edit_fooditem.html', data)

    

@login_required(login_url='login')
@user_passes_test(check_role_venders)
def delete_food(request,id=None):
    Fooditem = get_object_or_404(FoodItem, pk=id)
    Fooditem.delete()
    messages.success(request, 'Food Items has been deleted successfully!')

    return redirect('FoodItemByCategory',Fooditem.category.id)


#FoodItem CURD End 

        
    
    
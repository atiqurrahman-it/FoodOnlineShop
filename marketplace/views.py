from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render

from menu.models import Category, FoodItem
# Create your views here.
from vendor.models import Vendor


def Marketplace(request):
    vendors=Vendor.objects.filter(is_approved=True,user__is_active=True)
    vendor_count=vendors.count()
    data={
        "vendors":vendors,
        "vendor_count":vendor_count,
    }
    return render(request,'marketplace/listings.html',data)

def vendor_detail(request,vendor_slug):
    vendor=get_object_or_404(Vendor,vendor_slug=vendor_slug)
    categories=Category.objects.filter(vendor=vendor)
    user_items=FoodItem.objects.filter(vendor=vendor)

    single_vendor_all_itemls=[]
    for food in categories:
        vendor_all_itemls=FoodItem.objects.filter(vendor=vendor,category=food,is_available=True)
        single_vendor_all_itemls.append(vendor_all_itemls)


  
    data={
        "vendor":vendor,
        "categories":categories,
        "user_items":user_items,
        "single_vendor_all_itemls":single_vendor_all_itemls,
    }
    return render(request,'marketplace/vendor_detail.html',data)


def add_to_cart(request,food_id):
    if request.user.is_authenticated:
        return JsonResponse({'status': 'Success', 'message': 'user is login!'})
    else:
        return JsonResponse({'status': 'Failed', 'message': 'please login '})

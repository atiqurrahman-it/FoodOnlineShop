from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render

from marketplace.models import Cart
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
        # if request.is_ajax(): age ei ta user kora hoito
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            # check if food item exits 
            try:
                food_item=FoodItem.objects.get(id=food_id)
                # check if  the user has  already added that food to the cart

                try:
                    chkcart=Cart.objects.get(user=request.user,fooditem=food_item)
                    # increase the food quentity
                    chkcart.quantity +=1
                    chkcart.save()
                    return JsonResponse({'status': 'Success', 'message': 'increased the cart quantity!'})
                except:
                    chkcart=Cart.objects.create(user=request.user, fooditem=food_item,quantity=1)
                    return JsonResponse({'status': 'Success', 'message': 'added the food to the cart !'})


            except:
                return JsonResponse({'status': 'Success', 'message': 'this food does not exit !'})
                
        else:
            return JsonResponse({'status': 'Success', 'message': 'invalid request !'})
    else:
        return JsonResponse({'status': 'Failed', 'message': 'please login to continue '})

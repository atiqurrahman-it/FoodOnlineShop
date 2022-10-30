from django.shortcuts import render
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

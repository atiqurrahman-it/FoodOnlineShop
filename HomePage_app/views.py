from django.shortcuts import render

from vendor.models import Vendor

# Create your views here.

def Index(request):
    vendors=Vendor.objects.filter(is_approved=True,user__is_active=True)[:8]
    data={
        "vendors":vendors,
    }
    return render(request,'single_page/index.html',data)

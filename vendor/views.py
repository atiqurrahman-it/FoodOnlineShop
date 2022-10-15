from django.shortcuts import render

# Create your views here.

def Vprifile(request):
    return render(request,'vendor/profile.html')

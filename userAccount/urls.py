from django.urls import path
from . import views
urlpatterns = [
    path('registrationUser/',views.Register,name="registrationUser"),
     path('registrationVendor/',views.RegistrationVendor,name="registrationVendor")
]

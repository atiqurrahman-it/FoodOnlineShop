from django.urls import path

from . import views

urlpatterns = [
    path('registrationUser/',views.RegisterUser,name="registrationUser"),
    path('registrationVendor/',views.RegistrationVendor,name="registrationVendor"),
    path("login/",views.Login,name='login'),
    path("logout/",views.Logout,name='logout'),
    path("myaccount/",views.Myaccount,name='myaccount'),

    path('venderdashbord/',views.VenderDashbord,name="venderdashbord"),
    path('cousdashbord/',views.CousDashbord,name="cousdashbord")

]

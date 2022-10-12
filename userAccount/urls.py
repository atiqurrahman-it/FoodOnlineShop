from django.urls import path

from . import views

urlpatterns = [
    path('registrationUser/',views.RegisterUser,name="registrationUser"),
    path('registrationVendor/',views.RegistrationVendor,name="registrationVendor"),
    path("login/",views.Login,name='login'),
    path("logout/",views.Logout,name='logout'),
    path("myaccount/",views.Myaccount,name='myaccount'),

    path('venderdashbord/',views.VenderDashbord,name="venderdashbord"),
    path('cousdashbord/',views.CousDashbord,name="cousdashbord"),
    # email active path 
    path('activate/<uid>/<token>/',views.activate,name="activate"),
    # forgot password  start 
    path('forgot_password/',views.Forgot_password,name="forgot_password"),
    path('reset_password_validate/<uid>/<token>/',views.reset_password_validate,name="reset_password_validate"),
    path('reset_password',views.Reset_password,name='reset_password'),
    # forgot password end 

]

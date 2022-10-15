from django.urls import path,include

from . import views
urlpatterns = [
    # 127.0.0.1:8000/accounts/ ei path e click korle dashboard e niye jab 
    path('',views.Myaccount),
    # 127.0.0.1:8000/accounts/v or c dashboard 

    path('registrationUser/',views.RegisterUser,name="registrationUser"),
    path('registrationVendor/',views.RegistrationVendor,name="registrationVendor"),
    path("login/",views.Login,name='login'),
    path("logout/",views.Logout,name='logout'),
    path("myaccount/",views.Myaccount,name='myaccount'),

    path('vendordashbord/',views.VenderDashbord,name="venderdashbord"),
    path('cousdashbord/',views.CousDashbord,name="cousdashbord"),
    # email active path 
    path('activate/<uid>/<token>/',views.activate,name="activate"),
    # forgot password  start 
    path('forgot_password/',views.Forgot_password,name="forgot_password"),
    path('reset_password_validate/<uid>/<token>/',views.reset_password_validate,name="reset_password_validate"),
    path('reset_password',views.Reset_password,name='reset_password'),
    # forgot password end 



    # project er urls.py thek link up korlte partam korle path ta
    # path('vendor/',include('vendor.urls')),  online_project urls.py 
 
    # http://127.0.0.1:8000/vendor/profile ei ta hoito 

    path('vendor/',include('vendor.urls')),


]

from django.urls import path

from . import views

# userAccount theke include kora hoiche 

from userAccount import views as userAccountviews

urlpatterns = [
    # http://127.0.0.1:8000/accounts/vendor/ e click korle jano dashboard niye jai
    path('',userAccountviews.VenderDashbord,name='vendor'),


    path('profile',views.Vprifile,name='vprofile')
    
]

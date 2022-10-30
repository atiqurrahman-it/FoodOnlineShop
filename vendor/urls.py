from django.urls import path

from menu.models import FoodItem

from . import views

# userAccount theke include kora hoiche 

from userAccount import views as userAccountviews

urlpatterns = [
    # http://127.0.0.1:8000/accounts/vendor/ e click korle jano dashboard niye jai
    path('',userAccountviews.VenderDashbord,name='vendor'),


    path('profile',views.Vprifile,name='vprofile'),
    path('menue-builder',views.menue_builder,name='menue_builder'),
    path('menue-builder/category/<int:id>/',views.FoodItemByCategory,name='FoodItemByCategory'),
    
    #Category CURD
    path('menue-builder/category/add',views.add_category,name='add_category'),
    path('menu-builder/category/edit/<int:id>/',views.edit_category,name='edit_category'),
    path('menu-builder/category/delete/<int:id>/', views.delete_category, name='delete_category'),

    #FoodItem CURD
    path('menue-builder/food/add',views.add_food,name='add_food'),
    path('menu-builder/food/edit/<int:id>/',views.edit_food,name='edit_food'),
    path('menu-builder/food/delete/<int:id>/', views.delete_food, name='delete_food'),

    
    
]

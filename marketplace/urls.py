from django.urls import path
from . import views



urlpatterns = [
    path('', views.Marketplace,name='marketplace'),
    # cart # cart path ta vendor_detail er niche dile problem hobe 
    # path('cart/',views.cart,name='cart'), 
    # maim project e cart path niyechi

    path('<slug:vendor_slug>/', views.vendor_detail,name='vendor_detail'),

    #add to cart
    path('add_to_cart/<int:food_id>/', views.add_to_cart,name='add_to_cart'),

    # decrease  to cart
    path('decrease_cart/<int:food_id>/', views.decrease_cart,name='decrease_cart'),
   


]

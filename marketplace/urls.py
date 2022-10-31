from django.urls import path
from . import views



urlpatterns = [
    path('', views.Marketplace,name='marketplace'),
    path('<slug:vendor_slug>/', views.vendor_detail,name='vendor_detail'),
]

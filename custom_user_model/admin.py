from django.contrib import admin
from .models import User
# Register your models here.
from django.contrib.auth.admin import UserAdmin 

class customeUserAdmin(UserAdmin):
    # list_display =("email",)
    filter_horizontal=()
    list_filter=()
    fieldsets =()


admin.site.register(User, customeUserAdmin)

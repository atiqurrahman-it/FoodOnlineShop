from django.contrib import admin

from .models import Vendor

# Register your models here.
class vender_admin(admin.ModelAdmin):
    list_display=("user","vendor_name","is_approved","create_at")
    list_display_links=("user","vendor_name",)
    list_editable=('is_approved',)

admin.site.register(Vendor,vender_admin)

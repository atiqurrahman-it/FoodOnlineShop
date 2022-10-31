from django.contrib import admin

# Register your models here.
from .models import Cart


class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'fooditem', 'quantity', 'updated_at')
admin.site.register(Cart, CartAdmin)


# class TaxAdmin(admin.ModelAdmin):
#     list_display = ('tax_type', 'tax_percentage', 'is_active')
# admin.site.register(Tax, TaxAdmin)

from django.contrib import admin
from .models import Customer, Crab, Cart, Order, LineItem, CrabImage


class CrabImageAdmin(admin.TabularInline):
    model = CrabImage


class LineItemAdmin(admin.TabularInline):
    model = LineItem

#
# class CartAdmin(admin.TabularInline):
#     model = Cart


class CrabAdmin(admin.ModelAdmin):
    inlines = [CrabImageAdmin, ]


class OrderAdmin(admin.ModelAdmin):
    inlines = [LineItemAdmin, ]


class CustomerAdmin(admin.ModelAdmin):
    inlines = []


admin.site.register(Order, OrderAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Crab, CrabAdmin)

from django.contrib import admin
from .models import CartLineItem, Cart


class CartLineItemAdmin(admin.TabularInline):
    model = CartLineItem


class CartAdmin(admin.ModelAdmin):
    inlines = [CartLineItemAdmin, ]


admin.site.register(Cart, CartAdmin)

from django.contrib import admin
from .models import Order
from ..goods.models import LineItem


class OrderAdmin(admin.ModelAdmin):
    inlines = [ ]


admin.site.register(Order, OrderAdmin)

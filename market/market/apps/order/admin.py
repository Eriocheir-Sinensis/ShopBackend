from django.contrib import admin
from .models import Order
from ..goods.models import LineItem


class LineItemAdmin(admin.TabularInline):
    model = LineItem


class OrderAdmin(admin.ModelAdmin):
    inlines = [LineItemAdmin, ]


admin.site.register(Order, OrderAdmin)

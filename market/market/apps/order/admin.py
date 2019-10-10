from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdmin(admin.TabularInline):
    model = OrderLineItem


class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderLineItemAdmin, ]
    list_display = ('description', 'status',)


admin.site.register(Order, OrderAdmin)

from django.contrib import admin
from .models import Customer


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'address')
    readonly_fields = ('cid', )
    exclude = ('username', 'first_name', 'last_name', 'email', 'is_stuff', 'groups', 'user_permissions')
    inlines = []


admin.site.register(Customer, CustomerAdmin)

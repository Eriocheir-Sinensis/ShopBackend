from django.contrib import admin
from .models import Money


class MoneyAdmin(admin.ModelAdmin):
    list_display = ('name', 'enabled', 'pic')


admin.site.register(Money, MoneyAdmin)

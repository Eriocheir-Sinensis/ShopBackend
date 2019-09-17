from django.contrib import admin
from .models import Crab, CrabImage


class CrabImageAdmin(admin.TabularInline):
    model = CrabImage


class CrabAdmin(admin.ModelAdmin):
    inlines = [CrabImageAdmin, ]


admin.site.register(Crab, CrabAdmin)

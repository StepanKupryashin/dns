from django.contrib import admin
from .models import Components
# Register your models here.

@admin.register(Components)
class AdminComponents(admin.ModelAdmin):
    list_display = ("type", "name", "price",)
    search_fields = ("type", "name",)
    
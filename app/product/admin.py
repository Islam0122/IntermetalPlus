from django.contrib import admin
from .models import Product
from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from django.utils.translation import gettext as _


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'serial_number', 'model', 'manufacturer', 'price', 'created_at')
    list_filter = ('model', 'manufacturer')
    search_fields = ('name', 'model', 'manufacturer', 'serial_number')

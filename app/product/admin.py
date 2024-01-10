from .models import Product
from django.contrib import admin


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name',)


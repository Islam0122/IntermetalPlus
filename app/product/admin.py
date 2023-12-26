from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Product, Category
from django.utils.html import format_html

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_categories', 'price', 'created_at', 'updated_at')
    list_filter = ('category',)
    search_fields = ('name', 'category__title')

    def display_categories(self, obj):
        return ", ".join([category.title for category in obj.category.all()])
    display_categories.short_description = 'Categories'


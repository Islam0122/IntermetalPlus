from django.contrib import admin
from .models import Product, Category
from django.utils.translation import gettext_lazy as _


class RecommendationFilter(admin.SimpleListFilter):
    title = _('Рекомендация')
    parameter_name = 'is_recommended'

    def lookups(self, request, model_admin):
        return (
            ('all', _('Все товары')),
            ('recommended', _('Рекомендованные товары')),
        )

    def queryset(self, request, queryset):
        value = self.value()
        if value == 'recommended':
            return queryset.filter(is_recommended=True)
        elif value == 'all':
            return queryset.all()


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_categories', 'price', 'created_at', 'updated_at')
    list_filter = ('category', RecommendationFilter)
    search_fields = ('name', 'category__title')

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name == 'is_recommended':
            kwargs['widget'] = admin.widgets.AdminRadioSelect(choices=[(True, 'Да'), (False, 'Нет')])
        return super().formfield_for_dbfield(db_field, request, **kwargs)

    def display_categories(self, obj):
        return ", ".join([category.title for category in obj.category.all()])

    display_categories.short_description = 'Categories'

    def save_model(self, request, obj, form, change):
        if obj.is_recommended:
            recommended_count = Product.objects.filter(is_recommended=True).count()
            if recommended_count >= 3:
                self.message_user(request, "Cannot set more than three products as recommended.", level="error")
                obj.is_recommended = False
        super().save_model(request, obj, form, change)

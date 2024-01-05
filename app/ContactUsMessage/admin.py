from django.contrib import admin
from .models import ContactUsMessage


@admin.register(ContactUsMessage)
class ContactUsMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','contact_phone','created_at')
    search_fields = ('name', 'email', 'created_at')
    list_filter = ('created_at',)

    def has_add_permission(self, request):
        # Disable the "Add" button to prevent creating new records
        return False

    def has_change_permission(self, request, obj=None):
        # Disable the change permission to prevent modifying existing records
        return False

    def save_model(self, request, obj, form, change):
        # Disable saving the model to prevent updating existing records
        pass

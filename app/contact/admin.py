from django.contrib import admin
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone_number', 'whatsapp_number',)
    actions = None

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return Contact.objects.exists()


admin.site.register(Contact, ContactAdmin)


@receiver(post_migrate)
def create_about_us(sender, **kwargs):
    if Contact.objects.count() == 0:
        Contact.objects.create(
            email='intermetalplus2024@gmail.com',
            phone_number='+996500770009',
            whatsapp_number='+996500770009'
        )

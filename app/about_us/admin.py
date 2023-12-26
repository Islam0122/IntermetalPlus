from django.contrib import admin
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import AboutUs


class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('working_hours', 'address_url', 'contact_phone', 'contact_email', 'telegram_url')
    actions = None

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return AboutUs.objects.exists()


admin.site.register(AboutUs, AboutUsAdmin)


@receiver(post_migrate)
def create_about_us(sender, **kwargs):
    if AboutUs.objects.count() == 0:
        AboutUs.objects.create(
            working_hours='24/7',
            address_url='https://go.2gis.com/jsgykq',
            contact_phone='+996995121007',
            contact_email='default@example.com',
            telegram_url='https://t.me/islam1071'
        )

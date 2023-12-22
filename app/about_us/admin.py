from django.contrib import admin
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import AboutUs


class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('working_hours', 'contact_address', 'contact_phone', 'contact_email')
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
            working_hours='',
            contact_address='',
            contact_phone='',
            contact_email=''
        )
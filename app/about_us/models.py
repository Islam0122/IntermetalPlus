
from django.db import models



class AboutUs(models.Model):
    working_hours = models.CharField(max_length=100, verbose_name='Working Hours')
    contact_address = models.TextField(blank=True, null=True, verbose_name='Contact Address')
    contact_phone = models.CharField(max_length=200, blank=True, verbose_name='Contact Phone')
    contact_email = models.EmailField(verbose_name='Contact Email')

    class Meta:
        verbose_name_plural = 'About Us'

# class AboutUs(BaseModel):
#     working_hours = models.CharField(max_length=100, verbose_name='Working Hours')
#     contact_address = models.URLField(blank=True, null=True, verbose_name='address URL')
#     contact_phone = models.CharField(max_length=20, verbose_name='Contact Phone')
#     contact_email = models.EmailField(verbose_name='Contact Email')
#
#     # shop_name = models.CharField(max_length=255, verbose_name='Shop Name')
#     # description = models.TextField(verbose_name='Description')
#     # contact_address = models.CharField(max_length=255, verbose_name='Contact Address')
#     # telegram = models.URLField(blank=True, null=True, verbose_name='Telegram URL')
#     # instagram_url = models.URLField(blank=True, null=True, verbose_name='Instagram URL')

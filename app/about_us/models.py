from phonenumber_field.modelfields import PhoneNumberField

from app.basemodel.models import BaseModel
from django.db import models


class AboutUs(BaseModel):
    description = models.TextField(verbose_name='Description')
    working_hours = models.CharField(max_length=100, verbose_name='Working Hours',
                                     help_text='Specify the working hours.')
    address_url = models.URLField(blank=True, null=True, verbose_name='Address URL',
                                  help_text='URL of the contact address.')
    contact_phone = PhoneNumberField(blank=True, verbose_name='Contact Phone')
    contact_email = models.EmailField(verbose_name='Contact Email', help_text='Specify the contact email address.')
    telegram_url = models.URLField(blank=True, null=True, verbose_name='Telegram URL', help_text='URL for Telegram.')
    # instagram_url = models.URLField(blank=True, null=True, verbose_name='Instagram URL',
    # help_text='URL for Instagram.')

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'

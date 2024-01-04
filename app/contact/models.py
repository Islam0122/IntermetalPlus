from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Contact(models.Model):
    phone_number = PhoneNumberField(max_length=20)
    telegram_url = models.URLField(blank=True, null=True, verbose_name='Telegram URL', help_text='URL for Telegram.')
    instagram_url = models.URLField(blank=True, null=True, verbose_name='Instagram URL', help_text='URL for Instagram.')

    def __str__(self):
        return f"{self.phone_number} - {self.telegram_url or 'No Telegram'} - {self.instagram_url or 'No Instagram'}"

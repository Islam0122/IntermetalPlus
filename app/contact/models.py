from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Contact(models.Model):
    phone_number = PhoneNumberField(max_length=20, verbose_name='Номер телефона')
    telegram_url = models.URLField(
        blank=True,
        null=True,
        verbose_name='Ссылка на Telegram',
        help_text='URL для Telegram.'
    )
    instagram_url = models.URLField(
        blank=True,
        null=True,
        verbose_name='Ссылка на Instagram',
        help_text='URL для Instagram.'
    )
    def __str__(self):
        return f"{self.phone_number} - {self.telegram_url or 'No Telegram'} - {self.instagram_url or 'No Instagram'}"

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Contact(models.Model):
    phone_number = PhoneNumberField(max_length=20, verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Email')
    whatsapp_number = PhoneNumberField(max_length=20, verbose_name='Номер WhatsApp')

    def __str__(self):
        return f"{self.phone_number} | {self.email} | {self.whatsapp_number}"
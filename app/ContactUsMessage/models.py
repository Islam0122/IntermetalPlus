from app.basemodel.models import BaseModel
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.phonenumber import PhoneNumber


class ContactUsMessage(BaseModel):
    name = models.CharField(max_length=255, verbose_name='Name')
    email = models.EmailField(verbose_name='Email')
    message = models.TextField(verbose_name='Message')
    contact_phone = PhoneNumberField(blank=True, verbose_name='Contact Phone')
    def __str__(self):
        return f"Message from {self.name}"

    class Meta:
        verbose_name = 'Contact Us Message'
        verbose_name_plural = 'Contact Us Messages'

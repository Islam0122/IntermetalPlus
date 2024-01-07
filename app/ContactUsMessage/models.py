from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.mail import send_mail
from app.basemodel.models import BaseModel
from app.contact.models import Contact


class ContactUsMessage(BaseModel):
    name = models.CharField(max_length=255, verbose_name='Name')
    contact_phone = PhoneNumberField(blank=True, verbose_name='Contact Phone')
    email = models.EmailField(verbose_name='Email')
    message = models.TextField(verbose_name='Message')

    class Meta:
        verbose_name = 'Contact Us Message'
        verbose_name_plural = 'Contact Us Messages'
        ordering = ['-id']
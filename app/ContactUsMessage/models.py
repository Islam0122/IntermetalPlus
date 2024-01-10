from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.mail import send_mail
from app.basemodel.models import BaseModel
from app.contact.models import Contact


class ContactUsMessage(BaseModel):
    name = models.CharField(max_length=255, verbose_name='Название')
    contact_phone = models.CharField(max_length=20, verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Электронная почта')
    message = models.TextField(verbose_name='Сообщение')

    class Meta:
        verbose_name = 'Связаться с нами'
        verbose_name_plural = 'Связаться с нами'
        ordering = ['-id']
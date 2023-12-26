from django.core.mail import send_mail

from app.about_us.models import AboutUs
from app.basemodel.models import BaseModel
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.phonenumber import PhoneNumber


class ContactUsMessage(BaseModel):
    name = models.CharField(max_length=255, verbose_name='Name')
    email = models.EmailField(verbose_name='Email')
    message = models.TextField(verbose_name='Message')
    contact_phone = PhoneNumberField(blank=True, verbose_name='Contact Phone')

    def send_contact_email(self):
        subject = 'New Contact Us Message'
        message = (
            f'You have received a new message from {self.name}:\n'
            f'\n{self.message}\n'
            f'\nContact Email: {self.email}'
            f'\nContact Phone: {self.contact_phone}'
        )
        about_us = AboutUs.objects.first()
        to_email = about_us.contact_email

        # Send email
        send_mail(subject, message, self.email, [to_email])

    def __str__(self):
        return f"Message from {self.name}"

    class Meta:
        verbose_name = 'Contact Us Message'
        verbose_name_plural = 'Contact Us Messages'
        ordering = ['-id']
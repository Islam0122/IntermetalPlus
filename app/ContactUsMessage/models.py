
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


    def send_contact_email(self):
        subject = 'New Contact Us Message'
        message = (
            f'You have received a new message from {self.name}:\n'
            f'\n{self.message}\n'
            f'\nContact Email: {self.email}'
            f'\nContact Phone: {self.contact_phone}'
        )
        contact = Contact.objects.first()
        to_email = contact.email

        # Send email
        send_mail(subject, message, self.email, [to_email])

    def __str__(self):
        return f"Message from {self.name}"

    class Meta:
        verbose_name = 'Contact Us Message'
        verbose_name_plural = 'Contact Us Messages'
        ordering = ['-id']
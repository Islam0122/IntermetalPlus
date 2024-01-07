from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import ContactUsMessage
from .serializers import ContactUsMessageSerializer
from app.contact.models import Contact
from django.core.mail import send_mail
from django.core.mail import send_mail
from rest_framework import viewsets, status
from rest_framework.response import Response
import logging
from .models import ContactUsMessage
from .serializers import ContactUsMessageSerializer

class ContactUsMessageViewSet(viewsets.ModelViewSet):
    queryset = ContactUsMessage.objects.all()
    serializer_class = ContactUsMessageSerializer

    def send_contact_email(self, instance):
        subject = 'New Contact Us Message'
        message = (
            f'You have received a new message from {instance.name}:\n'
            f'\n{instance.message}\n'
            f'\nContact Email: {instance.email}'
            f'\nContact Phone: {instance.contact_phone}'
        )

        try:
            contact = Contact.objects.first()
            to_email = contact.email

            # Send email
            send_mail(subject, message, instance.email, [to_email])
            print('Email sent successfully 👌')

        except Exception as e:
            logging.error(f"An error occurred while sending email: {str(e)}")

    def perform_create(self, serializer):
        instance = serializer.save()
        self.send_contact_email(instance)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({'detail': 'Message sent successfully.'}, status=status.HTTP_201_CREATED, headers=headers)
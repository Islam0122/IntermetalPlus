
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import ContactUsMessage
from .serializers import ContactUsMessageSerializer


class ContactUsMessageViewSet(ModelViewSet):
    queryset = ContactUsMessage.objects.all()
    serializer_class = ContactUsMessageSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.send_contact_email()

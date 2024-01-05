
from rest_framework import generics
from rest_framework.response import Response
from .models import ContactUsMessage
from .serializers import ContactUsMessageSerializer


class ContactUsMessageCreateView(generics.CreateAPIView):
    queryset = ContactUsMessage.objects.all()
    serializer_class = ContactUsMessageSerializer

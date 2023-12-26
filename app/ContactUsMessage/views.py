from rest_framework import generics
from .models import ContactUsMessage
from .serializers import ContactUsMessageSerializer


class ContactUsMessageCreateView(generics.CreateAPIView):
    queryset = ContactUsMessage.objects.all()
    serializer_class = ContactUsMessageSerializer

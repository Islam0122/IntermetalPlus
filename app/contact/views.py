from rest_framework.viewsets import ModelViewSet
from .models import Contact
from .serializers import ContactSerializer


class ContactViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer



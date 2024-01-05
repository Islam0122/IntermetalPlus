from rest_framework import serializers
from .models import ContactUsMessage


class ContactUsMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUsMessage
        fields = [
                  'id',
                  'name',
                  'email',
                  'contact_phone',
                  'message',
                  'created_at'
                  ]
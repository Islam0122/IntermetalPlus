from rest_framework import serializers
from .models import Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = (
            'email',
            'phone_number',
            'telegram_url',
            'instagram_url',
        )

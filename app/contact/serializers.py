from rest_framework import serializers
from .models import Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'phone_number', 'email', 'whatsapp_number')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['Номер телефона'] = representation.pop('phone_number')
        representation['Email'] = representation.pop('email')
        representation['Номер WhatsApp'] = representation.pop('whatsapp_number')
        return representation
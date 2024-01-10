from rest_framework import serializers
from .models import ContactUsMessage

class ContactUsMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUsMessage
        fields = ('id', 'name', 'contact_phone', 'email', 'message')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['Название'] = representation.pop('name')
        representation['Номер телефона'] = representation.pop('contact_phone')
        representation['Электронная почта'] = representation.pop('email')
        representation['Сообщение'] = representation.pop('message')
        return representation
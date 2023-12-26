from rest_framework import serializers
from .models import AboutUs


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = (
            'working_hours',
            'address_url',
            'contact_phone',
            'contact_email',
            'telegram_url',
            # 'instagram_url',
        )

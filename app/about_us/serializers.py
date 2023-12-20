from rest_framework import serializers
from .models import AboutUs


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = ('id', 'working_hours', 'contact_address', 'contact_phone', 'contact_email')
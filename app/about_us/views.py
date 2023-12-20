
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import AboutUs
from .serializers import AboutUsSerializer


class About_UsViewSet(ModelViewSet):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer
    lookup_field = 'pk'


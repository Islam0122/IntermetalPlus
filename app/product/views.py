from django.shortcuts import render
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Category, Product
from .serializers import *


# Create your views here.
class CategoryViewSet(ModelViewSet):  # GET/PUT/DELETE/CREATE/POST
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'pk'


class ProductViewSet(ModelViewSet):  # GET/PUT/DELETE/CREATE/POST
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

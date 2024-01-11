from django.urls import path
from .views import ContactUsMessageViewSet

urlpatterns = [
    path('', ContactUsMessageViewSet.as_view({'post': 'create'}), name='contact-us')]

from django.urls import path
from .views import ContactUsMessageCreateView

urlpatterns = [
    path('', ContactUsMessageCreateView.as_view(), name='contact-us'),
]
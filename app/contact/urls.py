from django.urls import path
from . import views

urlpatterns = [
    path('', views.ContactViewSet.as_view({
        'get': 'list'
    }))]
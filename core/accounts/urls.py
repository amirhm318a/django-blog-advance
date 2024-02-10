from django.shortcuts import render
from django.urls import path,include
from . import views
from django.views.generic import TemplateView,RedirectView
app_name = 'accounts'
# Create your views here.

urlpatterns = [
    path('',include('django.contrib.auth.urls')),
    path('api/v1/',include('accounts.api.v1.urls')),
]
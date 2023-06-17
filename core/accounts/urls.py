from django.shortcuts import render
from django.urls import path,include
from . import views
from django.views.generic import TemplateView,RedirectView
app_name = 'acounts'
# Create your views here.

urlpatterns = [
    path('profile/<int:pk>',views.ProfileDetailView.as_view(),name='profile-detail'),
]
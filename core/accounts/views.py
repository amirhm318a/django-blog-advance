from django.shortcuts import render
from accounts.models import Profile
from django.views.generic import TemplateView,RedirectView
from django.views.generic import ListView,DetailView,FormView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin



class ProfileDetailView(DetailView):
    model = Profile

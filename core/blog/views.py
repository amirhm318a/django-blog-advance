from typing import Any, List, Sequence
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from .models import Post
from accounts.models import Profile
from django.views.generic import TemplateView,RedirectView
from django.views.generic import ListView,DetailView,FormView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from .forms import PostForm
# Create your views here.

# def indexView(request):
#     posts = Post.objects.all()
#     context = {'posts': posts}
#     return render(request,'index.html',context)

class IndexView(TemplateView):
    template_name = 'index.html'
    """super = TemplateView"""
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = 'https://maktabkhooneh.org/'
        return context

class RedirectToMaktab(RedirectView):
    url = 'https://maktabkhooneh.org/'
    
class PostListView(LoginRequiredMixin,ListView):
    # model = Post
    paginate_by = 2
    queryset = Post.objects.all()
    context_object_name = 'posts'
    ordering = '-id'

    # def get_queryset(self):
    #     posts = Post.objects.filter(status=1).order_by('-id').all()
    #     return posts
class PostDetailView(LoginRequiredMixin,DetailView):
    model = Post


class PostCreateView(FormView):
    template_name = 'contact.html'
    form_class = PostForm
    success_url = '/blog/post/'

    def form_valid(self,form):
        form.save()
        return super().form_valid(form)


class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    # fields = ['author','title','content','status','category','published_date']
    template_name = 'blog/form.html'
    form_class = PostForm    
    success_url = '/blog/post/'

class PostEditView(LoginRequiredMixin,UpdateView):
    model = Post
    form_class = PostForm
    success_url = '/blog/post/'


class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = '/blog/post/'
    

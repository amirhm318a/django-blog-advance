from rest_framework import generics
from django_filters import rest_framework as filters
from ...models import Post

from ...models import Post

class ProductFilter(filters.FilterSet):
    

    class Meta:
        model = Post 
        fields = ['category','author','status']
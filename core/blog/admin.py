from django.contrib import admin
from .models import Post,Category
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','author','status','category','created_date','published_date')
    list_filter = ('author','status','category')
    search_fields = ('title',)
admin.site.register(Category)
admin.site.register(Post,PostAdmin)
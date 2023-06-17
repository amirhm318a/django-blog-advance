from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from .models import User,Profile
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
# Register your models here.

    



class CustomUserAdmin(UserAdmin):
    models = User
    list_display=('email','is_superuser','is_active')
    list_filter = ('email','is_superuser','is_active')
    search_fields = ('email',)
    ordering = ('email',)
    fieldsets =(
        ("Authentication",{
            "fields":(
                'email','password'
            ),
        }),
        ("premissions",{
            "fields":(
                'is_staff','is_active','is_superuser'
            ),
        }),
        ("group_premissions",{
            "fields":(
                'groups','user_permissions'
            ),
        }),
        ("important date",{
            "fields":(
                'last_login',
            ),
        }),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1","password2", "is_staff",
                "is_active", "is_superuser"
            )}
        ),
    )


admin.site.register(Profile)
admin.site.register(User,CustomUserAdmin)
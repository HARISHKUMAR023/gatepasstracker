from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models.models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'user_type')
    list_editable = ('user_type',)

admin.site.register(CustomUser, CustomUserAdmin)
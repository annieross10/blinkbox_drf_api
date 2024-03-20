from django.contrib import admin
from .models import Profile

admin.site.register(Profile)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'owner', 'bio', 'birth_date', 'profile_picture']
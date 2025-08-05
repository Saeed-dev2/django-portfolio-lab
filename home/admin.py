from django.contrib import admin
from .models import Profile, Experience, Education

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'email', 'updated_at']
    search_fields = ['name', 'title', 'email']

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['position', 'company', 'start_date', 'end_date', 'is_current', 'order']
    list_filter = ['is_current', 'start_date']
    search_fields = ['position', 'company']
    ordering = ['-order', '-start_date']

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['degree', 'institution', 'start_date', 'end_date']
    list_filter = ['start_date']
    search_fields = ['degree', 'institution']
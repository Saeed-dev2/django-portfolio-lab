from django.contrib import admin
from .models import SkillCategory, Skill, Certification

@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'order']
    ordering = ['order', 'name']

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'proficiency', 'years_experience', 'is_featured', 'order']
    list_filter = ['category', 'proficiency', 'is_featured']
    search_fields = ['name', 'description']
    ordering = ['category', 'order', 'name']

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ['name', 'issuing_organization', 'issue_date', 'expiry_date']
    list_filter = ['issuing_organization', 'issue_date']
    search_fields = ['name', 'issuing_organization']
    filter_horizontal = ['skills']
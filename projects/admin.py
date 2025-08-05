from django.contrib import admin
from .models import Project, Technology, ProjectImage

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'is_featured', 'order', 'created_at']
    list_filter = ['status', 'is_featured', 'technologies']
    search_fields = ['title', 'description']
    filter_horizontal = ['technologies']
    inlines = [ProjectImageInline]

@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon', 'color']
    search_fields = ['name']

@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ['project', 'caption', 'order']
    list_filter = ['project']
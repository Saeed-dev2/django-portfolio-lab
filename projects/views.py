from django.views.generic import ListView, DetailView
from .models import Project, Technology

class ProjectListView(ListView):
    model = Project
    template_name = 'projects/projects.html'
    context_object_name = 'projects'
    paginate_by = 6

    def get_queryset(self):
        queryset = Project.objects.all()
        status = self.request.GET.get('status')
        tech = self.request.GET.get('tech')
        
        if status:
            queryset = queryset.filter(status=status)
        if tech:
            queryset = queryset.filter(technologies__id=tech)
            
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['technologies'] = Technology.objects.all()
        context['selected_status'] = self.request.GET.get('status', '')
        context['selected_tech'] = self.request.GET.get('tech', '')
        return context

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/project_detail.html'
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_projects'] = Project.objects.exclude(
            pk=self.object.pk
        ).filter(
            technologies__in=self.object.technologies.all()
        ).distinct()[:3]
        return context
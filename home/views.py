from django.views.generic import TemplateView
from .models import Profile, Experience, Education
from projects.models import Project
from skills.models import Skill

class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.first()
        context['experiences'] = Experience.objects.all()[:3]  # Latest 3
        context['education'] = Education.objects.all()[:2]     # Latest 2
        context['featured_projects'] = Project.objects.filter(is_featured=True)[:3]
        context['top_skills'] = Skill.objects.filter(is_featured=True)[:6]
        return context

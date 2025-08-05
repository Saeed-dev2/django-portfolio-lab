from django.views.generic import TemplateView
from .models import SkillCategory, Skill, Certification

class SkillsView(TemplateView):
    template_name = 'skills/skills.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['skill_categories'] = SkillCategory.objects.prefetch_related('skills').all()
        context['featured_skills'] = Skill.objects.filter(is_featured=True)
        context['certifications'] = Certification.objects.all()
        
        # Calculate overall proficiency stats
        skills = Skill.objects.all()
        if skills:
            avg_proficiency = sum(skill.proficiency for skill in skills) / len(skills)
            context['avg_proficiency'] = round(avg_proficiency, 1)
            context['total_skills'] = skills.count()
            context['expert_skills'] = skills.filter(proficiency=5).count()
        
        return context
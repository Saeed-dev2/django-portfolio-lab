from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from home.models import Profile, Experience, Education
from projects.models import Project, Technology
from skills.models import SkillCategory, Skill
import datetime

class Command(BaseCommand):
    help = 'Populate database with sample data'

    def handle(self, *args, **options):
        self.stdout.write('Creating sample data...')
        
        # Create superuser if doesn't exist
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
            
        # Create profile
        profile, created = Profile.objects.get_or_create(
            name='John Developer',
            defaults={
                'title': 'Full Stack Developer',
                'bio': 'Passionate developer with expertise in Python, Django, and modern web technologies.',
                'email': 'john@example.com',
                'phone': '+1 (555) 123-4567',
                'location': 'San Francisco, CA',
                'linkedin_url': 'https://linkedin.com/in/johndeveloper',
                'github_url': 'https://github.com/johndeveloper',
            }
        )
        
        # Create technologies
        technologies_data = [
            {'name': 'Python', 'icon': 'fab fa-python', 'color': '#3776ab'},
            {'name': 'Django', 'icon': 'fas fa-server', 'color': '#092e20'},
            {'name': 'JavaScript', 'icon': 'fab fa-js', 'color': '#f7df1e'},
            {'name': 'React', 'icon': 'fab fa-react', 'color': '#61dafb'},
            {'name': 'HTML5', 'icon': 'fab fa-html5', 'color': '#e34f26'},
            {'name': 'CSS3', 'icon': 'fab fa-css3-alt', 'color': '#1572b6'},
        ]
        
        for tech_data in technologies_data:
            Technology.objects.get_or_create(
                name=tech_data['name'],
                defaults=tech_data
            )
        
        # Create skill categories and skills
        frontend_category, _ = SkillCategory.objects.get_or_create(
            name='Frontend Development',
            defaults={'icon': 'fas fa-laptop-code', 'order': 1}
        )
        
        backend_category, _ = SkillCategory.objects.get_or_create(
            name='Backend Development',
            defaults={'icon': 'fas fa-server', 'order': 2}
        )
        
        skills_data = [
            {'name': 'HTML5', 'category': frontend_category, 'proficiency': 5, 'icon': 'fab fa-html5'},
            {'name': 'CSS3', 'category': frontend_category, 'proficiency': 5, 'icon': 'fab fa-css3-alt'},
            {'name': 'JavaScript', 'category': frontend_category, 'proficiency': 4, 'icon': 'fab fa-js'},
            {'name': 'Python', 'category': backend_category, 'proficiency': 5, 'icon': 'fab fa-python'},
            {'name': 'Django', 'category': backend_category, 'proficiency': 4, 'icon': 'fas fa-server'},
        ]
        
        for skill_data in skills_data:
            Skill.objects.get_or_create(
                name=skill_data['name'],
                category=skill_data['category'],
                defaults=skill_data
            )
        
        self.stdout.write(
            self.style.SUCCESS('Successfully created sample data!')
        )
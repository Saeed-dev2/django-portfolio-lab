from django.db import models
from django.urls import reverse

class Technology(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=100, blank=True, help_text="CSS class for icon")
    color = models.CharField(max_length=7, default="#000000", help_text="Hex color code")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Technologies"

class Project(models.Model):
    STATUS_CHOICES = [
        ('completed', 'Completed'),
        ('in_progress', 'In Progress'),
        ('planned', 'Planned'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    detailed_description = models.TextField(blank=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    technologies = models.ManyToManyField(Technology, blank=True)
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='completed')
    is_featured = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('projects:detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-order', '-created_at']

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='projects/gallery/')
    caption = models.CharField(max_length=200, blank=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.project.title} - Image {self.order}"

    class Meta:
        ordering = ['order']
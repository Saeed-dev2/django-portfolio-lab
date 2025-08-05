from django.db import models

class SkillCategory(models.Model):
    name = models.CharField(max_length=100)
    order = models.IntegerField(default=0)
    icon = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order', 'name']
        verbose_name_plural = "Skill Categories"

class Skill(models.Model):
    PROFICIENCY_CHOICES = [
        (1, 'Beginner'),
        (2, 'Novice'),
        (3, 'Intermediate'),
        (4, 'Advanced'),
        (5, 'Expert'),
    ]

    name = models.CharField(max_length=100)
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE, related_name='skills')
    proficiency = models.IntegerField(choices=PROFICIENCY_CHOICES, default=3)
    years_experience = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    icon = models.CharField(max_length=100, blank=True)
    color = models.CharField(max_length=7, default="#000000")
    is_featured = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def get_proficiency_percentage(self):
        return (self.proficiency / 5) * 100

    def get_proficiency_display_custom(self):
        return dict(self.PROFICIENCY_CHOICES)[self.proficiency]

    class Meta:
        ordering = ['category', 'order', 'name']

class Certification(models.Model):
    name = models.CharField(max_length=200)
    issuing_organization = models.CharField(max_length=200)
    issue_date = models.DateField()
    expiry_date = models.DateField(blank=True, null=True)
    credential_id = models.CharField(max_length=200, blank=True)
    credential_url = models.URLField(blank=True)
    skills = models.ManyToManyField(Skill, blank=True)

    def __str__(self):
        return f"{self.name} - {self.issuing_organization}"

    class Meta:
        ordering = ['-issue_date']
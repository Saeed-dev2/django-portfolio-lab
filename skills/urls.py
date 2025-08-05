from django.urls import path
from .views import SkillsView

app_name = 'skills'

urlpatterns = [
    path('', SkillsView.as_view(), name='list'),
]
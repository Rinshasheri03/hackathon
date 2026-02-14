from django import forms
from .models import SkillPost

class SkillForm(forms.ModelForm):
    class Meta:
        model = SkillPost
        fields = ['topic', 'description', 'video']

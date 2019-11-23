from django.forms import ModelForm, Textarea, Form
from .models import Experience


class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = ['content']
        widgets = {
            'content': Textarea(attrs={'cols': 40, 'rows': 5})
        }

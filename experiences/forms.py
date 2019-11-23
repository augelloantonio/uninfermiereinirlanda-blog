from django.forms import ModelForm, Textarea, Form
from .models import Experience
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = ['content']
        widgets = {
            'content': SummernoteWidget(attrs={'style': 'border: none;'}),
        }

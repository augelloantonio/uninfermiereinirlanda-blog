from django.forms import ModelForm, Textarea, Form
from .models import Experience
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = ['titolo', 'contenuto']
        widgets = {
            'contenuto': SummernoteWidget(attrs={'style': 'border: none;'}),
        }

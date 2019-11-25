from django.forms import ModelForm, Textarea, Form
from .models import Career
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class CareerForm(ModelForm):
    class Meta:
        model = Career
        fields = ['titolo', 'contenuto', 'città',
                  'regione', 'email', 'numero_telefonico']
        widgets = {
            'contenuto': SummernoteWidget(attrs={'style': 'border: none;'}),
        }

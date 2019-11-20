from django.forms import ModelForm, Textarea, Form
from .models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': Textarea(attrs={'cols': 40, 'rows': 5})
        }

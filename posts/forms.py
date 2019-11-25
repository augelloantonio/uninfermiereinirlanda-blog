from django import forms
from .models import Post
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class BlogPostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('titolo', 'contenuto', 'tag')
        widgets = {
            'contenuto': SummernoteWidget(attrs={'style': 'border: none;'}),
        }

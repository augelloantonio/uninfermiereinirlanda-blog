from django import forms
from .models import Post
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class BlogPostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'content', 'tag')
        widgets = {
            'content': SummernoteWidget(attrs={'style': 'border: none;'}),
        }

from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Experience


class ExperienceAdmin(SummernoteModelAdmin):
    model = Experience
    summernote_fields = ('content',)
    list_display = ('author', 'published_date')
    list_filter = ['published_date', 'author']
    search_fields = ['author', 'title']


admin.site.register(Experience, ExperienceAdmin)

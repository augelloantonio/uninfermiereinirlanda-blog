from django.contrib import admin
from .models import Comment


class CommentAdmin(admin.ModelAdmin):
    model = Comment
    list_display = ('post', 'pub_date', 'user')
    list_filter = ['pub_date', 'post', 'user']
    search_fields = ['user']


admin.site.register(Comment, CommentAdmin)

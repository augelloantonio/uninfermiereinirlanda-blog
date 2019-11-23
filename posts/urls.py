from django.urls import path
from .views import get_blog, post_detail, create_or_edit_post

urlpatterns = [
    path('', get_blog, name='get_blog'),
    path('/<int:pk>/', post_detail, name='post_detail'),
    path('/new/', create_or_edit_post, name='new_post'),
    path('/<int:pk>/edit/', create_or_edit_post, name='edit_post')
]

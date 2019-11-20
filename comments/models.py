from django.db import models
from django.utils import timezone
from django.conf import settings
from posts.models import Post
from django.contrib.auth.models import User


class Comment(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.PROTECT, default=1)
    content = models.CharField(max_length=1500)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=False)
    pub_date = models.DateTimeField(
        blank=True, null=True, default=timezone.now)

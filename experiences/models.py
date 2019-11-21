from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Experience(models.Model):
    author = models.ForeignKey(User, unique=False,
                               on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=100000)
    published_date = models.DateTimeField(
        blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.author

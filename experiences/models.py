from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Experience(models.Model):
    author = models.ForeignKey(User, unique=False,
                               on_delete=models.CASCADE, default=1)
    titolo = models.CharField(max_length=200)
    contenuto = models.CharField(max_length=100000)
    published_date = models.DateTimeField(
        blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.titolo

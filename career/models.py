from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class Career(models.Model):
    author = models.ForeignKey(User, unique=False,
                               on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=100000)
    published_date = models.DateTimeField(
        blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)
    approved = models.BooleanField(default=False)
    città = models.CharField(max_length=200, null=False, blank=False)
    regione = models.CharField(max_length=200, null=False, blank=False)
    email = models.CharField(max_length=200, blank=True)
    numero_telefonico = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title

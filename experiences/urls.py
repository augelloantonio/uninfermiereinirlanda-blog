from django.urls import path
from .views import get_experiences

urlpatterns = [
    path('', get_experiences, name='get_experiences'),
]

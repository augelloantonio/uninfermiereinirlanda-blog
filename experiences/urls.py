from django.urls import path
from .views import get_experiences, get_experience_details

urlpatterns = [
    path('', get_experiences, name='get_experiences'),
    path('<int:id>/', get_experience_details, name='get_experience_details'),
]

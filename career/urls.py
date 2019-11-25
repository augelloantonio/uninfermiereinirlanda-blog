from django.urls import path
from .views import get_careers, get_career_details, add_career

urlpatterns = [
    path('', get_careers, name='get_careers'),
    path('<int:id>/', get_career_details, name='get_career_details'),
    path('aggiungi_esperienza/', add_career, name="add_career"),
]

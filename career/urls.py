from django.urls import path
from .views import get_careers, get_career_details, add_or_edit_career

urlpatterns = [
    path('', get_careers, name='get_careers'),
    path('<int:id>/', get_career_details, name='get_career_details'),
    path('aggiungi_offerta/', add_or_edit_career, name="add_career"),
    path('<int:pk>/modifica_offerta/', add_or_edit_career, name="edit_career"),
]

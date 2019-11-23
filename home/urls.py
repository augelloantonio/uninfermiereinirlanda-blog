from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import contact_us, nmbi_view, la_registrazione_view, application_view, documenti_view, passi_finali_view

urlpatterns = [
    path('', views.index, name='index'),
    path('contatti', views.contact_us, name='contact_us'),
    path('nmbi/', nmbi_view, name="nmbi"),
    path('nmbi_registrazione', la_registrazione_view, name="nmbi_registrazione"),
    path('nmbi_applicazione', application_view, name="nmbi_applicazione"),
    path('nmbi_documenti', documenti_view, name="nmbi_documenti"),
    path('nmbi_passifinali', passi_finali_view, name="nmbi_passifinali"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import RedirectView
from django.views.static import serve
from .settings import MEDIA_ROOT
from home.views import index
from home import urls as urls_home
from accounts import urls as urls_accounts
from posts import urls as urls_posts
from experiences import urls as urls_experiences


urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('home/', include(urls_home)),
    path('accounts/', include(urls_accounts)),
    path('blog/', include(urls_posts)),
    path('esperienze', include(urls_experiences)),
    re_path('media/(?P<path>.*)', serve, {'document_root': MEDIA_ROOT}),
]

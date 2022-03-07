"""programmers_hub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from main_page.views import main_page_view
from login_page.views import login_page_view
from register_page.views import register_page_view
from articles_page.views import redirect_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page_view),
    path('login/', login_page_view, name='login'),
    path('register/', register_page_view, name='register'),
    path('articles/', redirect_view, name='articles')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

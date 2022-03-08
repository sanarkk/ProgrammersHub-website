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

from account_page.views import account_page_view
from main_page.views import main_page_view
from login_page.views import login_page_view, logout_view
from news_page.views import news_page_view, show_new
from register_page.views import register_page_view
from articles_page.views import redirect_view, show_article

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page_view, name='main_page'),
    path('login/', login_page_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_page_view, name='register'),
    path('programmers_hub/article/<int:id>/', show_article, name='articless'),
    path('programmers_hub/', redirect_view, name='articles'),
    path('programmers_hub/account/', account_page_view, name='account_page'),
    path('programmers_hub/news/', news_page_view, name='news_page'),
    path('programmers_hub/news/<int:id>', show_new, name='show_new'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

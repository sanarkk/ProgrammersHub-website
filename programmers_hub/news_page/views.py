from django.shortcuts import render


# Create your views here.
from news_page.models import News


def news_page_view(request):
    news = News.objects.all()
    args = {'news': news}
    return render(request, 'news_page.html', args)


def show_new(request, id):
    news = News.objects.get(id=id)
    args = {'news': news}
    return render(request, 'show_new.html', args)
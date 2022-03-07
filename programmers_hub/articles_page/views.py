from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404

from articles_page.models import Article


def redirect_view(request):
    articles = Article.objects.all()
    args = {'articles': articles}
    return render(request, 'articles_page.html', args)


def show_article(request, id):
    articles = Article.objects.all()
    args = {'articles': articles}
    return render(request, 'article.html', args)
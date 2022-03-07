from django.shortcuts import redirect, render

from articles_page.models import Articles


def redirect_view(request):
    articles = Articles.objects.all()
    args = {'articles': articles}
    return render(request, 'articles_page.html', args)
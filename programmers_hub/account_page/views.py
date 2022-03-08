from django.shortcuts import render
from django.contrib.auth.models import User


# Create your views here.
def account_page_view(request):
    return render(request, 'account_page.html')
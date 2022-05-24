from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    template = 'portfolio/index.html'
    return render(request, template)

def transactions(request):
    return HttpResponse('Страница со всеми транзакциями')

def coin(request, slug):
    return HttpResponse('Страница конкретной монеты')

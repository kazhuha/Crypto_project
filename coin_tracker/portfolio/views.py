from django.shortcuts import get_object_or_404, render

from .models import Portfolio, Token, Transactions


def index(request):
    template = 'portfolio/index.html'
    text = 'Это главная страница портфолио'
    context = {
        'text': text
    }
    return render(request, template, context)


def token_list(request):
    template = 'portfolio/token_list.html'
    tokens = Portfolio.objects.filter(owner=request.user)
    context = {
        'tokens': tokens,
    }
    return render(request, template, context)


def token_detail(requset, pk):
    template = 'portfolio/token_detail.html'
    token = get_object_or_404(Token, pk=pk)
    context = {
        'token': token
    }
    return render(requset, template, context)


def transactions(request):
    template = 'portfolio/transactions.html'
    user = request.user
    transactions = Transactions.objects.filter(buyer=user)
    context = {
        'transactions': transactions,
        'user': user
    }
    return render(request, template, context)

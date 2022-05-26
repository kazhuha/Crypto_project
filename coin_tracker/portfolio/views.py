from django.shortcuts import get_object_or_404, render
from django.db.models import Sum

from .models import Portfolio, Transaction


def index(request):
    template = 'portfolio/index.html'
    text = 'Это главная страница портфолио'
    context = {
        'text': text
    }
    return render(request, template, context)


def transactions(request):
    template = 'portfolio/transactions.html'
    user = request.user
    transactions = Transaction.objects.filter(buyer=user)
    context = {
        'transactions': transactions,
        'user': user
    }
    return render(request, template, context)


def portfolio(requset):
    template = 'portfolio/portfolio.html'
    user = requset.user
    tokens = Portfolio.objects.filter(owner=user)
    for token in tokens:
        token_sum = Transaction.objects.filter(buyer=user, first_coin=token.coin).aggregate(Sum('amount'))
        token.amount = token_sum['amount__sum']
        token.save()
    context = {
        'tokens': tokens,
    }
    return render(requset, template, context)

from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView
from django.db.models import Sum

from .models import Portfolio, Transaction
from .forms import PortfolioForm, TransactionForm


def amount_calc(transactions, position):
    """Функция расчета кол-ва монет в портфеле"""
    buy_summ = transactions.filter(side='BUY').aggregate(
        Sum('amount')
    )['amount__sum']
    buy_fee = transactions.filter(side='BUY').aggregate(Sum('fee'))['fee__sum']
    sell_summ = transactions.filter(side='SELL').aggregate(
        Sum('amount')
    )['amount__sum']
    if buy_summ is None:
        buy_summ, buy_fee = 0, 0
    if sell_summ is None:
        sell_summ = 0
    total = buy_summ - buy_fee - sell_summ
    position.amount = total
    position.save()


def index(request):
    """Главной страница"""
    template = 'portfolio/index.html'
    text = 'Это главная страница портфолио'
    context = {
        'text': text
    }
    return render(request, template, context)


def portfolio(request):
    """Страница портфеля юзера"""
    template = 'portfolio/portfolio.html'
    tokens = Portfolio.objects.filter(owner=request.user)
    context = {
        'tokens': tokens
    }
    return render(request, template, context)


class PortfolioAddToken(CreateView):
    """Страница добавления токена в портфель с формой"""
    template_name = 'portfolio/porfolio_add_token.html'
    form_class = PortfolioForm
    success_url = '/portfolio/'


def token_detail(request, pk):
    """Страница конкретного токена"""
    template = 'portfolio/token_detail.html'
    position = get_object_or_404(Portfolio, pk=pk)
    transactions = Transaction.objects.filter(
        buyer=request.user,
        buy_or_sell=position.coin.pk
    )
    amount_calc(transactions, position)
    context = {
        'position': position,
        'transactions': transactions,
    }
    return render(request, template, context)


class PortfolioAddTransaction(CreateView):
    """Страница с добавлением тразакций"""
    template_name = 'portfolio/portfolio_add_transaction.html'
    form_class = TransactionForm
    success_url = '/portfolio/'

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.utils import timezone
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

from .models import Portfolio, Transaction, Token
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


def model_token_fill(request):
    "Заполняет БД токенами с Бинанса"
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'
    headers = {
      'Accepts': 'application/json',
      'X-CMC_PRO_API_KEY': 'b6ca85ee-b64c-44b2-9c42-a70398331754',
    }
    session = Session()
    session.headers.update(headers)
    try:
        response = session.get(url).json()
        data = response['data']
        for coin in data:
            name = coin['name']
            ticker = coin['symbol']
            slug = coin['slug']
            if not Token.objects.filter(name=name).exists():
                Token.objects.create(name=name, ticker=ticker, slug=slug)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
    template = 'portfolio/token_filled_success.html'
    return render(request, template)


def index(request):
    """Главной страница"""
    template = 'portfolio/index.html'
    text = 'Это главная страница портфолио'
    context = {
        'text': text
    }
    return render(request, template, context)


@login_required
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

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.success_url)


def token_detail(request, ticker):
    """Страница конкретного токена"""
    template = 'portfolio/token_detail.html'
    coin = get_object_or_404(Token, ticker=ticker)
    position = get_object_or_404(Portfolio, owner=request.user, coin=coin.pk)
    transactions = Transaction.objects.filter(
        buyer=request.user,
        buy_or_sell=coin.pk
    )
    paginator = Paginator(transactions, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    amount_calc(transactions, position)
    context = {
        'position': position,
        'page_obj': page_obj,
    }
    return render(request, template, context)


class PortfolioAddTransaction(CreateView):
    """Страница с добавлением тразакций"""
    template_name = 'portfolio/portfolio_add_transaction.html'
    form_class = TransactionForm

    def form_valid(self, form):
        token = get_object_or_404(
            Token,
            ticker=self.request.path.split('/')[2]
        )
        print(token.pk)
        self.object = form.save(commit=False)
        self.object.buy_or_sell = token
        self.object.buyer = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_initial(self, *args, **kwargs):
        initial = super(PortfolioAddTransaction, self).get_initial(**kwargs)
        initial['trans_date'] = timezone.now()
        return initial

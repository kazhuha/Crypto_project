from django.forms import ModelForm

from .models import Portfolio, Transaction


class PortfolioForm(ModelForm):
    class Meta:
        model = Portfolio
        fields = ('owner', 'coin')


class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = (
            'buyer',
            'side',
            'buy_or_sell',
            'buy_or_sell_for',
            'price',
            'amount',
            'fee',
            'trans_date'
        )

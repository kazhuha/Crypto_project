from django.contrib import admin

from .models import Portfolio, Token, Transaction


class TokenAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'ticker', 'slug')
    search_fields = ('name',)


class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('pk', 'owner', 'coin', 'amount')
    search_fields = ('owner',)
    list_filter = ('owner', 'coin',)


class TransactionAdmin(admin.ModelAdmin):
    list_display = (
        'buyer',
        'side',
        'buy_or_sell',
        'buy_or_sell_for',
        'price',
        'amount',
        'fee',
        'trans_date'
    )
    search_fields = ('buyer',)
    list_filter = ('buyer', 'buy_or_sell', 'buy_or_sell_for',)


admin.site.register(Token, TokenAdmin)
admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Transaction, TransactionAdmin)

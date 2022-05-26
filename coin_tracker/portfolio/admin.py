from django.contrib import admin

from .models import Portfolio, Token, Transactions


class TokenAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'ticker',)
    search_fields = ('ticker',)


class TransactionsAdmin(admin.ModelAdmin):
    list_display = (
        'tranaction_date',
        'first_coin',
        'second_coin',
        'side',
        'price',
        'amount',
        'comission',
        'comission_token',
        'buyer'
    )
    search_fields = ('side', 'first_coin', 'second_coin')


class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('owner', 'token',)
    search_fields = ('owner', 'token')


admin.site.register(Token, TokenAdmin)
admin.site.register(Transactions, TransactionsAdmin)
admin.site.register(Portfolio, PortfolioAdmin)

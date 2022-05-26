from django.contrib import admin

from .models import Transaction, Portfolio


class TransactionAdmin(admin.ModelAdmin):
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
    list_filter = ('side', 'first_coin', 'second_coin')


class PortfolioAdmin(admin.ModelAdmin):
    list_display = (
        'owner',
        'coin',
        'amount'
    )


admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Portfolio, PortfolioAdmin)

from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator


User = get_user_model()


class Token(models.Model):
    name = models.CharField(max_length=20, unique=True)
    ticker = models.CharField(max_length=10, unique=True)

    class Meta:
        verbose_name = 'Токен'
        verbose_name_plural = 'Токены'

    def __str__(self):
        return self.ticker


class Transactions(models.Model):
    buyer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='transactions'
    )
    SIDE_CHOICES = [
        ('BUY', 'Buy'),
        ('SELL', 'Sell')
    ]
    tranaction_date = models.DateField()
    first_coin = models.ForeignKey(
        Token,
        on_delete=models.CASCADE,
        related_name='transactions_fst'
    )
    second_coin = models.ForeignKey(
        Token,
        on_delete=models.CASCADE,
        related_name='transactions_snd'
    )
    side = models.CharField(max_length=4, choices=SIDE_CHOICES)
    price = models.FloatField(validators=[MinValueValidator(0)])
    amount = models.FloatField(validators=[MinValueValidator(0)])
    comission = models.FloatField(validators=[MinValueValidator(0)])
    comission_token = models.ForeignKey(
        Token,
        on_delete=models.CASCADE,
        related_name='comissions'
    )

    class Meta:
        verbose_name = 'Транзакция'
        verbose_name_plural = 'Транзакции'
        ordering = ['-tranaction_date']


class Portfolio(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='portfolio_token'
    )
    token = models.ForeignKey(
        Token,
        on_delete=models.CASCADE,
        related_name='portfolio'
    )

    class Meta:
        verbose_name = 'Портфель'
        verbose_name_plural = 'Портфели'

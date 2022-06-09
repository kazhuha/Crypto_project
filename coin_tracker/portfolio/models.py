from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils import timezone


User = get_user_model()


class Token(models.Model):
    """Модель для токенов"""
    name = models.CharField(
        max_length=30,
        unique=True,
        verbose_name='Название'
    )
    ticker = models.CharField(
        max_length=7,
        verbose_name='Тикер'
    )

    def __str__(self):
        return self.ticker

    class Meta:
        verbose_name = 'Токен'
        verbose_name_plural = 'Токены'


class Portfolio(models.Model):
    """Модель крипто-портфеля"""
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='portfolio'
    )
    coin = models.ForeignKey(
        Token,
        on_delete=models.CASCADE,
        related_name='portfolio'
    )
    amount = models.FloatField(
        validators=[MinValueValidator(0)],
        default=0,
        verbose_name='количество'
    )

    class Meta:
        verbose_name = 'Портфель'
        verbose_name_plural = 'Портфели'
        unique_together = ['owner', 'coin']


class Transaction(models.Model):
    """Модель транзакций по покупке и продажи крипты"""
    SIDE_CHOICES = [
        ('BUY', 'Buy'),
        ('SELL', 'Sell')
    ]
    buyer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='transaction'
    )
    side = models.CharField(
        max_length=4,
        choices=SIDE_CHOICES,
        default='BUY'
    )
    buy_or_sell = models.ForeignKey(
        Token,
        on_delete=models.CASCADE,
        related_name='transaction_buy'
    )
    buy_or_sell_for = models.ForeignKey(
        Token,
        on_delete=models.CASCADE,
        related_name='transaction_buy_for'
    )
    price = models.FloatField(
        validators=[MinValueValidator(0)]
    )
    amount = models.FloatField(
        validators=[MinValueValidator(0)]
    )
    fee = models.FloatField(
        validators=[MinValueValidator(0)]
    )
    trans_date = models.DateTimeField(
    )

    class Meta:
        verbose_name = 'Транзакция'
        verbose_name_plural = 'Транзакции'
        ordering = ['-trans_date']

    def get_absolute_url(self):
        return reverse('portfolio:detail', args=[self.buy_or_sell])

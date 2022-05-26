from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.forms import FloatField


User = get_user_model()

TOKEN_DICT = (
    ('BTC', 'Bitcoin'),
    ('ETH', 'Etherium'),
    ('USDT', 'Tether'),
    ('RUB', 'Russian ruble'),
)


class Transaction(models.Model):
    SIDE_CHOICES = [
        ('BUY', 'Buy'),
        ('SELL', 'Sell')
    ]
    buyer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='transactions'
    )
    tranaction_date = models.DateTimeField()
    first_coin = models.CharField(
        max_length=50,
        choices=sorted(TOKEN_DICT),
    )
    second_coin = models.CharField(
        max_length=50,
        choices=sorted(TOKEN_DICT)
    )
    side = models.CharField(
        max_length=4,
        choices=SIDE_CHOICES
    )
    price = models.FloatField(validators=[MinValueValidator(0)])
    amount = models.FloatField(validators=[MinValueValidator(0)])
    comission = models.FloatField(validators=[MinValueValidator(0)])
    comission_token = models.CharField(
        max_length=50,
        choices=sorted(TOKEN_DICT),
        blank=True
    )

    class Meta:
        verbose_name = 'Транзакция'
        verbose_name_plural = 'Транзакции'
        ordering = ['-tranaction_date']


class Portfolio(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='portfolio'
    )
    coin = models.CharField(
        max_length=50,
        choices=sorted(TOKEN_DICT)
    )
    amount = models.FloatField(
        validators=[MinValueValidator(0)],
        default=0
    )

    class Meta:
        verbose_name = 'Портфолио'
        verbose_name_plural = 'Портфолио'

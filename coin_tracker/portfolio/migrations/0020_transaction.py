# Generated by Django 2.2.19 on 2022-05-27 10:54

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('portfolio', '0019_portfolio_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('amount', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('fee', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('trans_date', models.DateTimeField()),
                ('buy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transaction_buy', to='portfolio.Token')),
                ('buy_for', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transaction_buy_for', to='portfolio.Token')),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transaction', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Транзакция',
                'verbose_name_plural': 'Транзакции',
            },
        ),
    ]

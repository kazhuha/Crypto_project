# Generated by Django 2.2.19 on 2022-05-26 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0010_auto_20220526_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='comission_token',
            field=models.CharField(choices=[('BTC', 'Bitcoin    '), ('ETH', 'Etherium'), ('USDT', 'Tether')], max_length=50),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='first_coin',
            field=models.CharField(choices=[('BTC', 'Bitcoin    '), ('ETH', 'Etherium'), ('USDT', 'Tether')], max_length=50),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='second_coin',
            field=models.CharField(choices=[('BTC', 'Bitcoin    '), ('ETH', 'Etherium'), ('USDT', 'Tether')], max_length=50),
        ),
    ]

# Generated by Django 2.2.19 on 2022-05-26 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_auto_20220526_0728'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transactions',
            options={'ordering': ['-tranaction_date'], 'verbose_name': 'Транзакция', 'verbose_name_plural': 'Транзакции'},
        ),
    ]
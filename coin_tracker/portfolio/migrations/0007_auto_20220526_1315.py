# Generated by Django 2.2.19 on 2022-05-26 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_auto_20220526_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='token',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='portfolio_token', to='portfolio.Token'),
        ),
    ]

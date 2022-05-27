# Generated by Django 2.2.19 on 2022-05-27 07:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('portfolio', '0015_auto_20220527_0728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='name',
            field=models.CharField(max_length=30, unique=True, verbose_name='Название'),
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='portfolio', to='portfolio.Token')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='portfolio', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Портфель',
                'verbose_name_plural': 'Портфели',
            },
        ),
    ]

# Generated by Django 4.1.7 on 2023-04-19 11:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='structure',
            name='chef',
        ),
        migrations.RemoveField(
            model_name='structure',
            name='pct_city',
        ),
        migrations.AddField(
            model_name='structure',
            name='chief',
            field=models.CharField(blank=True, max_length=35, null=True, verbose_name='Начальник Подразделения'),
        ),
        migrations.AddField(
            model_name='structure',
            name='percent_city',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(99)], verbose_name='Процент города'),
        ),
        migrations.AlterField(
            model_name='structure',
            name='name',
            field=models.CharField(blank=True, max_length=35, null=True, verbose_name='Название Подразделения'),
        ),
        migrations.AlterField(
            model_name='structure',
            name='phone',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Телефон'),
        ),
    ]

# Generated by Django 4.1.7 on 2023-04-22 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_remove_historicalcar_body_remove_historicalcar_brand_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='gov_number',
            field=models.CharField(blank=True, max_length=16, null=True, verbose_name='Номер государственной регистрации'),
        ),
        migrations.AlterField(
            model_name='car',
            name='register_number',
            field=models.CharField(blank=True, max_length=16, null=True, verbose_name='Реестровый номер'),
        ),
    ]

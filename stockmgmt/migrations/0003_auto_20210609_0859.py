# Generated by Django 2.2 on 2021-06-09 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockmgmt', '0002_stock_exp_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='last_updated',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

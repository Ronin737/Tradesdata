# Generated by Django 4.0.1 on 2022-01-20 23:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Trades', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trade',
            name='trade_details',
        ),
        migrations.AddField(
            model_name='tradedetails',
            name='trade_item',
            field=models.ForeignKey(default=None, help_text='The details of the trade, i.e. price, quantity', on_delete=django.db.models.deletion.CASCADE, to='Trades.trade', verbose_name='tradeDetails'),
        ),
    ]
from datetime import datetime
from email.policy import default
from enum import unique
from statistics import mode
from django.db import models
from django_extensions.db.fields import AutoSlugField



class TradeDetails(models.Model):
    buysellindicator=models.CharField(max_length=4,choices=[('BUY','BUY'),('SELL','SELL')],help_text='A value of BUY for buys, SELL for sells')
    price=models.FloatField(help_text='The price of the Trade')
    quantity=models.IntegerField(help_text='The amount of units traded')


    class Meta:
        verbose_name='Trade Detail'


class Trade(models.Model):
    asset_Class=models.CharField('assetClass',max_length=60,default=None,help_text='The asset class of the instrument traded. E.g. Bond, Equity, FX...etc')
    counterparty=models.CharField(max_length=100,default=None,help_text="The counterparty the trade was executed with. May not always be available")
    instrument_Id=models.CharField('instrumentId',max_length=10,help_text="The ISIN/ID of the instrument traded. E.g. TSLA, AAPL, AMZN...etc")
    instrument_Name=models.CharField('instrumentName',max_length=20,help_text='The name of the instrument traded')
    trader=models.CharField(max_length=100,help_text='The name of the Trader')
    trade_date_time=models.DateTimeField('tradeDateTime',help_text="The date-time the Trade was executed")
    trade_id=AutoSlugField('tradeId',populate_from=['instrument_Id','trader'],unique=True)
    trade_details=models.OneToOneField(TradeDetails,on_delete=models.CASCADE,help_text="The details of the trade, i.e. price, quantity",verbose_name='tradeDetails',default=None)


    class Meta:
        get_latest_by='trade_date_time'
        ordering=['instrument_Name']










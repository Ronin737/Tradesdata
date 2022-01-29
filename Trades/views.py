from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.generics import ListAPIView
from .models import Trade
from .serialisers import TradeSerializer
from django.db.models import Q 
from datetime import datetime as dt

class DisplayTradeAPI(ReadOnlyModelViewSet):
    queryset=Trade.objects.all()
    serializer_class=TradeSerializer
    lookup_field='trade_id'

class SearchTradeAPI(ListAPIView):
    serializer_class=TradeSerializer

    def get_queryset(self):
        searchbase=self.kwargs['searchparam']
        queryset=Trade.objects.filter(Q(counterparty__iexact=searchbase)|Q(trader__iexact=searchbase)|Q(instrument_Id__iexact=searchbase)|Q(instrument_Name__iexact=searchbase))
        return queryset

class SingleFilterTradeAPI(ListAPIView):
    serializer_class=TradeSerializer

    def get_queryset(self):
        if('assetClass' in self.kwargs):
            queryset=Trade.objects.filter(asset_Class__iexact=self.kwargs['assetClass'])
            return queryset
        elif('minPrice'in self.kwargs):
            queryset=Trade.objects.filter(trade_details__price__gte=self.kwargs['minPrice'])
            return queryset
        elif('maxPrice'in self.kwargs):
            queryset=Trade.objects.filter(trade_details__price__lte=self.kwargs['maxPrice'])
            return queryset
        elif('start'in self.kwargs):
            filterbase=dt.fromisoformat(self.kwargs['start'])
            queryset=Trade.objects.filter(trade_date_time__gte=filterbase)
            return queryset
        elif('end'in self.kwargs):
            filterbase=dt.fromisoformat(self.kwargs['end'])
            queryset=Trade.objects.filter(trade_date_time__lte=filterbase)
            return queryset
        else:
            queryset=Trade.objects.filter(trade_details__buysellindicator__iexact=self.kwargs['tradeType'])
            return queryset
    


class RangeFilterTradeAPI(ListAPIView):

    serializer_class=TradeSerializer

    def get_queryset(self):
        if('minPrice' in self.kwargs):
            queryset=Trade.objects.filter(trade_date_time__gte=self.kwargs['minPrice']).filter(trade_date_time__lte=self.kwargs['maxPrice'])
            return queryset
        else:
            start=dt.fromisoformat(self.kwargs['start'])
            end=dt.fromisoformat(self.kwargs['end'])
            queryset=Trade.objects.filter(trade_date_time__gte=start).filter(trade_date_time__lte=end)
            return queryset


            
        




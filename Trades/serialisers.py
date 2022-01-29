from django.forms import fields
from rest_framework.serializers import ModelSerializer
from .models import TradeDetails,Trade

class TradeDetailsSerializer(ModelSerializer):

    class Meta:
        model=TradeDetails
        fields='__all__'
    
    

class TradeSerializer(ModelSerializer):
    class Meta:
        model=Trade
        fields='__all__'
    
    trade_details=TradeDetailsSerializer()



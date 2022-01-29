from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import DisplayTradeAPI,SearchTradeAPI,SingleFilterTradeAPI,RangeFilterTradeAPI

router=SimpleRouter()
router.register('trade',DisplayTradeAPI,basename='api-trade')
api=router.urls

urlpatterns=api+[path('search/<str:searchparam>/',SearchTradeAPI.as_view(),name='api-trade-search'),
                path('filter/<str:assetClass>/',SingleFilterTradeAPI.as_view(),name='api-trade-filter-asset'),
                path('filter/<str:tradeType>/',SingleFilterTradeAPI.as_view(),name='api-trade-filter-tradetype'),
                path('filter/<int:maxPrice>/',SingleFilterTradeAPI.as_view(),name='api-trade-filter-maxprice'),
                path('filter/<int:minPrice>/',SingleFilterTradeAPI.as_view(),name='api-trade-filter-minprice'),
                path('filter/<str:start>/',SingleFilterTradeAPI.as_view(),name='api-trade-filter-startdate'),
                path('filter/<str:end>/',SingleFilterTradeAPI.as_view(),name='api-trade-filter-enddate'),
                path('filter/<int:minPrice>/<int:maxPrice>/',RangeFilterTradeAPI.as_view(),name='api-trade-filter-pricerange'),
                path('filter/<str:start>/<str:end>/',RangeFilterTradeAPI.as_view(),name='api-trade-filter-daterange')]


                
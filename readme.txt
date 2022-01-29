1. Django and django-restframework used for development of API endpoints. All dependencies defined in requirements.txt.
2. Program contains 1 app named Trades.
3. The data models are defined in Trades.models.py.
4. Since each trade will have a unique trade detail, a one-to-one relationship has been defined between Trade and Tradedetails.
5. The outputs are serialised to JSON strings, and the serialisers for the model data are stored in serialisers.py.
6. The valid url with API endpoints are defined in urls.py. API endpoints have been defined for listing trades, retrieving a trade, searching for specific trades and filtering out trades.
7. The API actions are defined via class based views and viewsets in views.py. 
8. Since a lot of the API actions are generic, django's generics library has been used to define the actions. For retrieval and listing, the generic viewset for read-only methods has been used. For filtering and searching, the generic ListAPIView has been used with an overriden get_queryset method for modifying the queryset.
9. The endpoints can be accessed by specifying the correct url from root url. No root homepage has been defined however.
10. The database can be accessed via the django-admin access.


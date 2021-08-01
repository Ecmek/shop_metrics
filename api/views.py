from django.db.models import Sum
from rest_framework import generics

from .filters import ShopFilter
from .models import Shop
from .serializers import ShopSerializer


class ShopList(generics.ListAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    filterset_class = ShopFilter

    def get_queryset(self):
        queryset = Shop.objects.all()
        groups = dict(self.request.GET).get('group')
        if groups:
            queryset = queryset.values(*groups).annotate(visitors=Sum('visitors'), earnings=Sum('earnings'))
        return queryset

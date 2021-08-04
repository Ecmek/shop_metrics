from rest_framework import generics
from django.db.models import Sum

from .filters import ShopFilter
from .models import Shop
from .serializers import ShopSerializer


class ShopList(generics.ListAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    filterset_class = ShopFilter

    def get_queryset(self):
        queryset = Shop.objects.all()
        groups = self.request.GET.getlist('group')
        if groups:
            shows = self.request.GET.getlist('show')
            queryset = queryset.values(*groups).annotate(**{show: Sum(show) for show in shows})
        return queryset

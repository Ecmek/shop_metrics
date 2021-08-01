from django_filters import rest_framework as filters

from .models import Shop


class ShopFilter(filters.FilterSet):
    date_from = filters.DateFilter(field_name="date", lookup_expr='gte')
    date_to = filters.DateFilter(field_name="date", lookup_expr='lte')
    o = filters.OrderingFilter(fields=('date', 'shop', 'country', 'visitors', 'earnings'))

    class Meta:
        model = Shop
        fields = ['date_from', 'date_to', 'date', 'country', 'shop', 'visitors', 'earnings']

from rest_framework import generics

from .filters import ShopFilter, get_annotation
from .models import Shop
from .serializers import ShopSerializer


class ShopList(generics.ListAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    filterset_class = ShopFilter

    def get_queryset(self):
        queryset = Shop.objects.all()
        groups = self.request.GET.getlist('group')
        shows = self.request.GET.getlist('show')
        if groups:
            queryset = queryset.values(*groups).annotate(**get_annotation(shows))
        return queryset

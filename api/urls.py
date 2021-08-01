from django.urls import path

from .views import ShopList

urlpatterns = [
    path('v1/metrics/',  ShopList.as_view()),
]

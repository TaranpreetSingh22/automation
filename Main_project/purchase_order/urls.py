# orders/urls.py

from django.urls import path
from .views import purchase_order

urlpatterns = [
    path('create/', purchase_order, name='purchase_order'),
]

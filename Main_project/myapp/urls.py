# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('procurement-request/', views.procurement_request, name='procurement_request'),
]

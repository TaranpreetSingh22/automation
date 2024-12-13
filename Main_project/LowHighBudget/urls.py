from django.urls import path
from . import views

app_name = "LowHighBudget"

urlpatterns = [
    path('', views.procurement_request_view, name='procurement_request'),
]

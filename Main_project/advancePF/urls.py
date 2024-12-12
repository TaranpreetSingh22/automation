from django.urls import path
from . import views

app_name = "advancePF"

urlpatterns = [
    path('', views.procurement_request_view, name='procurement_request'),
    path('advance/', views.advance_request_view, name='advance_request'),
]

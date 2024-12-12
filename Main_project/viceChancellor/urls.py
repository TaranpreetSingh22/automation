# viceChancellor/urls.py

from django.urls import path
from . import views

app_name = 'viceChancellor'

urlpatterns = [
    path('', views.vc_dashboard, name='vc_dashboard'),
    path('approve-quotation/<int:quotation_id>/', views.approve_quotation, name='approve_quotation'),
    path('reject-quotation/<int:quotation_id>/', views.reject_quotation, name='reject_quotation'),
]

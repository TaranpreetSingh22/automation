# viceChancellor/urls.py

from django.urls import path
from . import views

app_name = 'viceChancellor'

urlpatterns = [
    path('', views.vc_dashboard, name='vc_dashboard'),
    path('approve/<int:request_id>/', views.approve_request, name='approve_request'),
    path('reject/<int:request_id>/', views.reject_request, name='reject_request'),
]

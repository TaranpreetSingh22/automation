from django.urls import path
from . import views

urlpatterns = [
    path('', views.procurement_request_view, name='procurement_request'),
    path('success/', views.success_view, name='success'),  # Success view if needed
]

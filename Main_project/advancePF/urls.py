from django.urls import path
from . import views

urlpatterns = [
    path('procurement/', views.procurement_request_view, name='procurement_request'),
    path('advance/', views.advance_request_view, name='advance_request'),
]

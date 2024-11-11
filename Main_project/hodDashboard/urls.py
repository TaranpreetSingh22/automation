# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('hod/', views.hod_dashboard, name='hod_dashboard'),
]

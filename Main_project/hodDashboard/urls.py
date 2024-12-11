# myapp/urls.py
from django.urls import path
from . import views

app_name = 'hodDashboard'

urlpatterns = [
    path('', views.hod_dashboard, name='hod_dashboard'),
]

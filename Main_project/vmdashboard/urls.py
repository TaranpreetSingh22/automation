from django.urls import path
from . import views

app_name = 'vmdashboard'

urlpatterns = [
    path('', views.vendor_list, name='vendor_list'),
    path('add/', views.add_vendor, name='add_vendor'),
]
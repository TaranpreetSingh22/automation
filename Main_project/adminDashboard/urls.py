from django.urls import path
from . import views

app_name = 'adminDashboard'

urlpatterns = [
    path('', views.admin_page, name='admin_page'),
    path('add/', views.add_user, name='add_user'),
]

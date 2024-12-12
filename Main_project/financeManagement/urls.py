# urls.py
from django.urls import path
from . import views

app_name = "financeManagement"

urlpatterns = [
    path('', views.finance_dashboard, name='finance_dashboard'),
    path('send_to_hod/<int:quotation_id>/', views.send_to_hod, name='send_to_hod'),
]
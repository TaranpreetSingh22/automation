from django.urls import path
from . import views

urlpatterns = [
    path('', views.registrar_dashboard, name='registrar_dashboard'),
]

from django.urls import path
from . import views

app_name = 'registrar'

urlpatterns = [
    path('', views.registrar_dashboard, name='registrar_dashboard'),
]

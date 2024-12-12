from django.urls import path
from . import views

app_name = 'registrar'

urlpatterns = [
    path('', views.registrar_dashboard, name='registrar_dashboard'),
    path('approve-quotation/<int:quotation_id>/', views.approve_quotation, name='approve_quotation'),
    path('reject-quotation/<int:quotation_id>/', views.reject_quotation, name='reject_quotation'),
    path('send-to-vc/<int:quotation_id>/', views.send_to_vc, name='send_to_vc'),
]

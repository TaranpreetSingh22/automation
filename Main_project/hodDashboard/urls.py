# myapp/urls.py
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'hodDashboard'

urlpatterns = [
    path('', views.hod_dashboard, name='hod_dashboard'),
    path('approve-quotation/<int:quotation_id>/', views.approve_quotation, name='approve_quotation'),
    path('reject-quotation/<int:quotation_id>/', views.reject_quotation, name='reject_quotation'),
    path('send-to-registrar/<int:quotation_id>/', views.send_to_registrar, name='send_to_registrar'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

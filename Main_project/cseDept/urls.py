from django.urls import path
from .views import *

app_name = "cseDept"

urlpatterns = [
    path('', cse, name='cse'),
    path('reqQuot/', reqQuot, name='reqQuot'),
    path('save-quotation/', save_quotation, name='save_quotation'),
]

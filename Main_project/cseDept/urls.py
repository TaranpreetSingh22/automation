from django.urls import path
from .views import cse, reqQuot

urlpatterns = [
    path('', cse, name='cse'),
    path('reqQuot/', reqQuot, name='reqQuot')
]

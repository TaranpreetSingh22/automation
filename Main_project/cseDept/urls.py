from django.urls import path
from .views import cse, deptcse, reqQuot

urlpatterns = [
    path('', cse, name='cse'),
    path('deptcse/', deptcse, name='deptcse'),
    path('reqQuot/', reqQuot, name='reqQuot')
]

# myapp/views.py
from django.shortcuts import render
from .models import Purpose

def hod_dashboard(request):
    purposes = Purpose.objects.all()  # Query all purpose entries from the database
    return render(request, 'myApp/hod_dashboard.html', {'purposes': purposes})

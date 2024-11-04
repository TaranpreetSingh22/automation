# purchase/views.py

from django.shortcuts import render, redirect
from .models import PurchaseRequest

def vc_dashboard(request):
    purchase_requests = PurchaseRequest.objects.all()
    return render(request, 'viceChancellor/vc_dashboard.html', {'purchase_requests': purchase_requests})

def approve_request(request, request_id):
    purchase_request = PurchaseRequest.objects.get(id=request_id)
    purchase_request.approval_status = 'Approved'
    purchase_request.save()
    return redirect('vc_dashboard')

def reject_request(request, request_id):
    purchase_request = PurchaseRequest.objects.get(id=request_id)
    purchase_request.approval_status = 'Rejected'
    purchase_request.save()
    return redirect('vc_dashboard')

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from registrar.models import VCQuotations

def vc_dashboard(request):
    # Fetch all HOD quotations to display in the table
    quotations = VCQuotations.objects.all()
    context = {'quotations': quotations}
    return render(request, 'viceChancellor/vc_dashboard.html', context)

def approve_quotation(request, quotation_id):
    # Approve the quotation
    quotation = get_object_or_404(VCQuotations, id=quotation_id)
    quotation.status = 'Approved'
    quotation.save()
    messages.success(request, 'Quotation approved successfully!')
    return redirect('viceChancellor:vc_dashboard')

def reject_quotation(request, quotation_id):
    # Reject the quotation
    quotation = get_object_or_404(VCQuotations, id=quotation_id)
    quotation.status = 'Rejected'
    quotation.save()
    messages.error(request, 'Quotation rejected.')
    return redirect('viceChancellor:vc_dashboard')
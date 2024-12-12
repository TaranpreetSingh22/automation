from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import RegistrarQuotations
from financeManagement.models import HODQuotation

def hod_dashboard(request):
    # Fetch all HOD quotations to display in the table
    quotations = HODQuotation.objects.all()
    context = {'quotations': quotations}
    return render(request, 'myApp/hod_dashboard.html', context)

def approve_quotation(request, quotation_id):
    # Approve the quotation
    quotation = get_object_or_404(HODQuotation, id=quotation_id)
    quotation.status = 'Approved'
    quotation.save()
    messages.success(request, 'Quotation approved successfully!')
    return redirect('hodDashboard:hod_dashboard')

def reject_quotation(request, quotation_id):
    # Reject the quotation
    quotation = get_object_or_404(HODQuotation, id=quotation_id)
    quotation.status = 'Rejected'
    quotation.save()
    messages.error(request, 'Quotation rejected.')
    return redirect('hodDashboard:hod_dashboard')

def send_to_registrar(request, quotation_id):
    # Fetch the quotation and send to Registrar
    quotation = get_object_or_404(HODQuotation, id=quotation_id)

    if quotation.uploaded_pdf:
        # Create a new RegistrarQuotation object
        RegistrarQuotations.objects.create(
            vendor_name=quotation.vendor_name,
            item=quotation.item,
            quantity=quotation.quantity,
            total_cost=quotation.total_cost,
            uploaded_pdf=quotation.uploaded_pdf,
            status='Pending',
        )
        messages.success(request, 'Quotation sent to Registrar successfully!')
    else:
        messages.error(request, 'No uploaded PDF found for this quotation.')

    return redirect('hodDashboard:hod_dashboard')

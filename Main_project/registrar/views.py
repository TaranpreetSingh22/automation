from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import VCQuotations
from hodDashboard.models import RegistrarQuotations

def registrar_dashboard(request):
    # Fetch all HOD quotations to display in the table
    quotations = RegistrarQuotations.objects.all()
    context = {'quotations': quotations}
    return render(request, 'rg_dashboard.html', context)

def approve_quotation(request, quotation_id):
    # Approve the quotation
    quotation = get_object_or_404(RegistrarQuotations, id=quotation_id)
    quotation.status = 'Approved'
    quotation.save()
    messages.success(request, 'Quotation approved successfully!')
    return redirect('registrar:registrar_dashboard')

def reject_quotation(request, quotation_id):
    # Reject the quotation
    quotation = get_object_or_404(RegistrarQuotations, id=quotation_id)
    quotation.status = 'Rejected'
    quotation.save()
    messages.error(request, 'Quotation rejected.')
    return redirect('registrar:registrar_dashboard')

def send_to_vc(request, quotation_id):
    # Fetch the quotation and send to Registrar
    quotation = get_object_or_404(RegistrarQuotations, id=quotation_id)

    if quotation.uploaded_pdf:
        # Create a new RegistrarQuotation object
        VCQuotations.objects.create(
            vendor_name=quotation.vendor_name,
            item=quotation.item,
            quantity=quotation.quantity,
            total_cost=quotation.total_cost,
            uploaded_pdf=quotation.uploaded_pdf,
            status='Pending',
        )
        messages.success(request, 'Quotation sent to VC successfully!')
    else:
        messages.error(request, 'No uploaded PDF found for this quotation.')

    return redirect('registrar:registrar_dashboard')

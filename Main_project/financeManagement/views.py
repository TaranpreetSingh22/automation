from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from .models import HODQuotation
from cseDept.models import QuotationDetails
from hodDashboard.models import RegistrarQuotations
from registrar.models import VCQuotations
from itertools import chain

# View to display the Finance Dashboard
def finance_dashboard(request):
    # Fetch all quotations to display in the table
    quotations = QuotationDetails.objects.all()
    context_one = {'quotations': quotations}
    #return render(request, 'financeDashboard.html', context)

    # Fetching data from each table
    hod_approvals = HODQuotation.objects.all().values(
        "id", "vendor_name", "status"
    )
    for record in hod_approvals:
        record["source"] = "hod"

    registrar_approvals = RegistrarQuotations.objects.all().values(
        "id", "vendor_name", "status"
    )
    for record in registrar_approvals:
        record["source"] = "registrar"

    vc_approvals = VCQuotations.objects.all().values(
        "id", "vendor_name", "status"
    )
    for record in vc_approvals:
        record["source"] = "vc"

    # Combine all records into a single list
    combined_approvals = list(chain(hod_approvals, registrar_approvals, vc_approvals))

    context_two = {
        "combined_approvals": combined_approvals,
    }

    context = {**context_one, **context_two}
    return render(request, "financeDashboard.html", context)
   
def send_to_hod(request, quotation_id):
    if request.method == 'POST':
        # Fetch the QuotationDetails instance
        quotation = get_object_or_404(QuotationDetails, id=quotation_id)

        # Get the uploaded PDF from the form (optional for sending to HOD)
        uploaded_pdf = request.FILES.get('quotation_file')

        # If the file is provided, create HODQuotation instance
        if uploaded_pdf:
            # Create a HODQuotation instance with the necessary details
            HODQuotation.objects.create(
                vendor_name=quotation.vendor,
                item=quotation.item,
                quantity=quotation.quantity,
                total_cost=quotation.total_cost,
                uploaded_pdf=uploaded_pdf,  # Save the file here
                status='Pending'
            )
            messages.success(request, 'Quotation sent to HOD successfully!')
        else:
            messages.error(request, 'No file uploaded. Please upload a file to send to HOD.')

        return redirect('financeManagement:finance_dashboard')

    return redirect('financeManagement:finance_dashboard')

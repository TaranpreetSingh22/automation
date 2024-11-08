from django.shortcuts import render, redirect
from .models import ProcurementRequest, AdvanceRequest, Vendor, VendorQuote
from .forms import ProcurementRequestForm, VendorQuoteForm, AdvanceRequestForm

def procurement_request_view(request):
    if request.method == 'POST':
        # Handle Procurement Request Form
        procurement_form = ProcurementRequestForm(request.POST)
        if procurement_form.is_valid():
            procurement_request = procurement_form.save()

            # Handle Vendor Quote Form
            vendor_quote_forms = []
            for i in range(int(request.POST.get('vendor_count', 0))):
                vendor_quote_form = VendorQuoteForm(request.POST)
                if vendor_quote_form.is_valid():
                    vendor_quote_form.save()

            return redirect('procurement_success')
    else:
        procurement_form = ProcurementRequestForm()

    return render(request, 'advancePF/procurement_form.html', {'procurement_form': procurement_form})


def advance_request_view(request):
    if request.method == 'POST':
        form = AdvanceRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('advance_success')
    else:
        form = AdvanceRequestForm()

    return render(request, 'advancePF/advance_request_form.html', {'form': form})

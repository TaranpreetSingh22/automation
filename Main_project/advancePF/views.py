from django.shortcuts import render, redirect
from .models import ProcurementRequest, AdvanceRequest, VendorQuote
from .forms import ProcurementRequestForm, VendorQuoteForm, AdvanceRequestForm
from vmdashboard.models import Vendor
from django.http import HttpResponse
from django.shortcuts import render, redirect
from reportlab.pdfgen import canvas
from io import BytesIO
from .forms import ProcurementRequestForm, VendorQuoteForm
from django.contrib import messages

def procurement_request_view(request):
    vendors = Vendor.objects.all()
    
    if request.method == 'POST':
        # Handle Procurement Request Form
        procurement_form = ProcurementRequestForm(request.POST)
        
        if procurement_form.is_valid():
            # Save ProcurementRequest to DB
            procurement_request = procurement_form.save()

            # Handle Vendor Quote Form
            vendor_data = []
            vendor_count = int(request.POST.get('vendor_count', 0))
            error_found = False

            for i in range(vendor_count):
                vendor_name = request.POST.get(f'vendor_name_{i + 1}')
                quote = request.POST.get(f'quote_{i + 1}')

                # Check if vendor name and quote are provided
                if vendor_name and quote:
                    vendor = Vendor.objects.filter(name=vendor_name).first()

                    if vendor:
                        # Create VendorQuote and associate it with the procurement request
                        vendor_quote = VendorQuote(
                            procurement_request=procurement_request,
                            vendor=vendor,
                            quote=quote
                        )
                        vendor_quote.save()  # Save VendorQuote to DB
                        vendor_data.append({'vendor_name': vendor_name, 'quote': quote})
                    else:
                        error_found = True
                        messages.error(request, f"Vendor '{vendor_name}' does not exist.")
                        break
                else:
                    error_found = True
                    messages.error(request, "Please provide both vendor name and quote.")
                    break

            if error_found:
                # If there was an error, render the form again with messages
                return render(request, 'advancePF/procurement_form.html', {
                    'procurement_form': procurement_form,
                    'vendors': vendors,
                })

            # Generate PDF after form submission (this part works as expected)
            buffer = BytesIO()
            p = canvas.Canvas(buffer)

            # Title and procurement request details
            p.drawString(100, 800, f"Procurement Request: {procurement_request.description}")
            y_position = 750
            p.drawString(100, y_position, f"Description: {procurement_request.description}")
            y_position -= 20

            # Add vendor quotes to PDF
            for idx, vendor in enumerate(vendor_data, 1):
                p.drawString(100, y_position, f"Vendor {idx}: {vendor['vendor_name']}")
                y_position -= 20
                p.drawString(100, y_position, f"Quote: {vendor['quote']}")
                y_position -= 40

            p.showPage()
            p.save()

            # Move the buffer position to the beginning
            buffer.seek(0)

            # Return the PDF as a response
            response = HttpResponse(buffer, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="procurement_request.pdf"'

            # Success message after saving and PDF generation
            messages.success(request, "Procurement Request submitted successfully and PDF generated!")
        
            return response  # Return the generated PDF as the response

    else:
        procurement_form = ProcurementRequestForm()

    return render(request, 'advancePF/procurement_form.html', {
        'procurement_form': procurement_form,
        'vendors': vendors,
    })



def advance_request_view(request):
    if request.method == 'POST':
        # Retrieve the form data from the POST request
        from_user = request.POST.get('from')
        date = request.POST.get('date')
        invoice_date = request.POST.get('invoice_date')
        amount = request.POST.get('amount')
        amount_words = request.POST.get('amount_words')
        company = request.POST.get('company')
        purpose = request.POST.get('purpose')
        account_user = request.POST.get('account_user')

        # Create and save the AdvanceRequest instance
        advance_request = AdvanceRequest(
            from_user=from_user,
            date=date,
            invoice_date=invoice_date,
            amount=amount,
            amount_words=amount_words,
            company=company,
            purpose=purpose,
            account_user=account_user
        )

        # Save the data to the database
        advance_request.save()

        # Display success message
        messages.success(request, 'Advance request submitted successfully.')

        # Redirect to a success page
        return redirect('advancePF:advance_request')  # Make sure to set this view

    else:
        return render(request, 'advancePF/advance_request_form.html')

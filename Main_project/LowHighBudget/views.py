from django.shortcuts import render, redirect
from .forms import ProcurementRequestForm
from django.http import HttpResponse
from django.contrib import messages
from .models import ProcurementRequest


def procurement_request_view(request):
    if request.method == 'POST':
        form = ProcurementRequestForm(request.POST)
        if form.is_valid():
            budget_type = form.cleaned_data['budget_type']

            # Create the data dictionary based on budget type
            if budget_type == "low":
                data = {
                    'budget_type': form.cleaned_data['budget_type'],
                    'item': form.cleaned_data['item'],
                    'purpose': form.cleaned_data['purpose'],
                    'cost': form.cleaned_data['cost'],
                    'vendor': form.cleaned_data['vendor'],
                    'person_responsible': form.cleaned_data['person_responsible'],
                    'subject': form.cleaned_data['subject'],
                    'date': form.cleaned_data['date'],
                }
            elif budget_type == "high":
                data = {
                    'budget_type': form.cleaned_data['budget_type'],
                    'from_field': form.cleaned_data['from_field'],
                    'product': form.cleaned_data['product'],
                    'high_budget_vendor': form.cleaned_data['high_budget_vendor'],
                    'amount': form.cleaned_data['amount'],
                    'high_budget_subject': form.cleaned_data['high_budget_subject'],
                    'content': form.cleaned_data['content'],
                    'high_budget_date': form.cleaned_data['high_budget_date'],
                }

            # Save data to the database
            ProcurementRequest.objects.create(**data)
            messages.success(request, "Procurement request submitted successfully!")
            return redirect("LowHighBudget:procurement_request")
        else:
            print(form.errors)
            messages.error(request, "There was an error in your submission. Please try again.")
    else:
        form = ProcurementRequestForm()

    return render(request, 'LowHighBudget/procurement_request_form.html', {'form': form})
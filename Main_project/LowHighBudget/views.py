from django.shortcuts import render, redirect
from .forms import ProcurementRequestForm
from django.http import HttpResponse

def procurement_request_view(request):
    if request.method == 'POST':
        form = ProcurementRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to a success page or another URL
    else:
        form = ProcurementRequestForm()
    return render(request, 'LowHighBudget/procurement_request_form.html', {'form': form})

def success_view(request):
    return HttpResponse("Request submitted successfully!")

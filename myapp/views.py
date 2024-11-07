# myapp/views.py
from django.shortcuts import render
from .forms import ProcurementForm

def procurement_request(request):
    form = ProcurementForm()
    if request.method == "POST":
        form = ProcurementForm(request.POST)
        if form.is_valid():
            # Handle form data here
            # form.cleaned_data['field_name'] to access form data
            return render(request, 'myapp/success.html')
    return render(request, 'myapp/procurement_form.html', {'form': form})

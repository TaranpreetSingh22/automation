from django.shortcuts import render, redirect
from .models import Vendor
from .forms import VendorForm
from django.urls import reverse
from django.contrib import messages

def add_vendor(request):
    if request.method == 'POST':
        form = VendorForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')  # Assuming the form has a 'name' field
            if Vendor.objects.filter(name=name).exists():
                messages.error(request, f"Vendor '{name}' already exists.")
            else:
                form.save()
                messages.success(request, f"Vendor '{name}' added successfully.")
                return redirect('vmdashboard:vendor_list')
    else:
        form = VendorForm()
    
    return render(request, 'vmdashboard/add_vendor.html', {'form': form})

def vendor_list(request):
    vendors = Vendor.objects.all()
    return render(request, 'vmdashboard/vendor_list.html', {'vendors': vendors})


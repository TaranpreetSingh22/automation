from django.shortcuts import render, redirect
from .models import Vendor
from .forms import VendorForm

def vendor_list(request):
    vendors = Vendor.objects.all()
    return render(request, 'vmdashboard/vendor_list.html', {'vendors': vendors})

def add_vendor(request):
    if request.method == 'POST':
        form = VendorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vendor_list')
    else:
        form = VendorForm()
    return render(request, 'vendors/add_vendor.html', {'form': form})

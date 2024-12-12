from django.shortcuts import render, redirect
from .forms import PurchaseOrderForm, OrderItemFormSet
from django.contrib import messages

def purchase_order(request):
    if request.method == "POST":
        # Initialize forms with submitted data
        form = PurchaseOrderForm(request.POST, request.FILES)
        formset = OrderItemFormSet(request.POST)

        if form.is_valid() and formset.is_valid():
            # Save the main PurchaseOrder object
            purchase_order = form.save()

            # Save the related OrderItem objects
            order_items = formset.save(commit=False)
            for item in order_items:
                item.purchase_order = purchase_order  # Link each item to the main PurchaseOrder
                item.save()

            # Optional: Add success message
            messages.success(request, "Purchase Order created successfully!")
            return redirect('purchase_order:purchase_order')  # Redirect to a success page or another view
        else:
            # Optional: Add error message
            messages.error(request, "Please correct the errors below.")
    else:
        # Initialize empty forms for GET request
        form = PurchaseOrderForm()
        formset = OrderItemFormSet()

    return render(request, 'purchase_order/purchase_order.html', {'form': form, 'formset': formset})


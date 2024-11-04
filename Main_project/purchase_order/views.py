from django.shortcuts import render, redirect
from .forms import PurchaseOrderForm, OrderItemFormSet

def purchase_order(request):
    if request.method == 'POST':
        form = PurchaseOrderForm(request.POST, request.FILES)
        formset = OrderItemFormSet(request.POST)
        
        if form.is_valid() and formset.is_valid():
            purchase_order = form.save()
            order_items = formset.save(commit=False)
            for item in order_items:
                item.order = purchase_order
                item.save()
            return redirect('purchase_order_success')
    else:
        form = PurchaseOrderForm()
        formset = OrderItemFormSet()

    return render(request, 'purchase_order/purchase_order.html', {
        'form': form,
        'formset': formset,
    })

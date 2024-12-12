from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import QuotationDetails
from vmdashboard.models import Vendor
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib import messages

# Create your views here.
def cse(request):
    return render(request, 'cseDept/cse.html')

def reqQuot(request):
    vendors = Vendor.objects.all()
    return render(request, 'cseDept/request_quotation.html', {'vendors': vendors})

@csrf_exempt
def save_quotation(request):
    if request.method == 'POST':
        data = request.POST
        vendor_id = data['vendor']
        item = data['item']
        quantity = data['quantity']
        price_unit = data['price_unit']
        total_cost = data['total_cost']

        # Save to the database
        QuotationDetails.objects.create(
            vendor_id=vendor_id,
            item=item,
            quantity=quantity,
            price_per_unit=price_unit,
            total_cost=total_cost
        )

    # Return JSON response
        return JsonResponse({
            'message': 'Quotation saved successfully!',
            'vendor': vendor_id,
            'item': item,
            'quantity': quantity,
            'price_unit': price_unit,
            'total_cost': total_cost,
        })
    
    return JsonResponse({'error': 'Invalid request.'}, status=400)

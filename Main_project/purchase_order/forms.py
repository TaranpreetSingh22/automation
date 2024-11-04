# orders/forms.py

from django import forms
from .models import PurchaseOrder, OrderItem

class PurchaseOrderForm(forms.ModelForm):
    class Meta:
        model = PurchaseOrder
        fields = [
            'ref', 'date', 'to_address', 'instruments', 'quotation_no', 
            'quotation_date', 'branchname', 'terms', 'total', 'total_gst', 
            'pf', 'grand_total_no_gst', 'grand_total', 'pdf'
        ]

class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = [
            'item_code', 'description', 'hsn_code', 'qty', 'unit_price', 
            'total', 'gst_percentage', 'total_with_gst'
        ]

from django.forms import inlineformset_factory

OrderItemFormSet = inlineformset_factory(
    PurchaseOrder, OrderItem, form=OrderItemForm, extra=1, can_delete=True
)

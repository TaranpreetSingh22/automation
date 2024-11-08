from django import forms
from .models import ProcurementRequest, AdvanceRequest, Vendor, VendorQuote

class ProcurementRequestForm(forms.ModelForm):
    class Meta:
        model = ProcurementRequest
        fields = ['description']

class VendorQuoteForm(forms.ModelForm):
    class Meta:
        model = VendorQuote
        fields = ['vendor', 'quote']


class AdvanceRequestForm(forms.ModelForm):
    class Meta:
        model = AdvanceRequest
        fields = ['from_user', 'date', 'invoice_date', 'amount', 'amount_words', 'company', 'purpose', 'account_user']

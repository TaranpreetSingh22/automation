# forms.py
from django import forms

class ProcurementRequestForm(forms.Form):
    BUDGET_CHOICES = [
        ('low', 'Low Budget'),
        ('high', 'High Budget'),
    ]

    # Define fields
    budget_type = forms.ChoiceField(choices=BUDGET_CHOICES, widget=forms.RadioSelect, label="Budget Type")
    
    # Fields for Low Budget
    item = forms.CharField(max_length=100, label="Item")
    purpose = forms.CharField(max_length=255, label="Purpose", required=False)
    cost = forms.DecimalField(max_digits=10, decimal_places=2, label="Cost (Rs)", required=False)
    vendor = forms.CharField(max_length=255, label="Vendor", required=False)
    person_responsible = forms.CharField(max_length=255, label="Person Responsible", required=False)
    subject = forms.CharField(max_length=255, label="Subject", required=False)
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label="Date", required=False)
    
    # Fields for High Budget
    from_field = forms.CharField(max_length=100, label="From", required=False)
    product = forms.CharField(max_length=255, label="Product", required=False)
    high_budget_vendor = forms.CharField(max_length=255, label="Vendor", required=False)
    amount = forms.DecimalField(max_digits=10, decimal_places=2, label="Amount (Rs)", required=False)
    high_budget_subject = forms.CharField(max_length=255, label="Subject", required=False)
    content = forms.CharField(widget=forms.Textarea, label="Content", required=False)
    high_budget_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label="Date", required=False)

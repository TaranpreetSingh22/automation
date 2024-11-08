# myapp/forms.py
from django import forms

class ProcurementForm(forms.Form):
    item = forms.CharField(label="Item", max_length=100, required=True)
    purpose = forms.CharField(label="Purpose", max_length=200, required=True)
    cost = forms.DecimalField(label="Cost (Rs)", max_digits=10, decimal_places=2, required=True)
    vendor = forms.CharField(label="Vendor", max_length=100, required=True)
    person_responsible = forms.CharField(label="Person Responsible", max_length=100, required=True)
    subject = forms.CharField(label="Subject", max_length=100, required=True)
    date = forms.DateField(label="Date", widget=forms.TextInput(attrs={'type': 'date'}), required=True)
    comments = forms.CharField(label="Comments", widget=forms.Textarea(attrs={'rows': 3}), required=False)

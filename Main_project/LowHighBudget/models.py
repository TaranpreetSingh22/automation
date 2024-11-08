from django.db import models

class ProcurementRequest(models.Model):
    BUDGET_CHOICES = [
        ('low', 'Low Budget'),
        ('high', 'High Budget'),
    ]

    # Common fields
    budget_type = models.CharField(max_length=10, choices=BUDGET_CHOICES)
    item = models.CharField(max_length=100, blank=True, null=True)
    purpose = models.TextField(blank=True, null=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    vendor = models.CharField(max_length=100, blank=True, null=True)
    person_responsible = models.CharField(max_length=100, blank=True, null=True)
    subject = models.CharField(max_length=200, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)  # For high budget form

    def __str__(self):
        return f"{self.item or self.product} - {self.budget_type}"

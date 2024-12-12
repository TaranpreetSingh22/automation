from django.db import models

# Create your models here.

class HODQuotation(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending HOD Approval'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]

    vendor_name = models.CharField(max_length=255)
    item = models.CharField(max_length=255)
    quantity = models.IntegerField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    uploaded_pdf = models.FileField(upload_to='quotations/')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"HOD Quotation {self.id} - {self.vendor_name}"

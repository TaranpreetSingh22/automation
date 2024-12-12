from django.db import models

# Create your models here.

class VCQuotations(models.Model):
    vendor_name = models.CharField(max_length=255)
    item = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    uploaded_pdf = models.FileField(upload_to='quotations/')
    status = models.CharField(max_length=50, default='Pending')
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.vendor_name} - {self.item}"

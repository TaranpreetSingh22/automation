from django.db import models
from vmdashboard.models import Vendor
# Create your models here.

class QuotationDetails(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    item = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField()
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    total_cost = models.DecimalField(max_digits=15, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

from django.db import models

# Create your models here.
# purchase/models.py

from django.db import models

class PurchaseRequest(models.Model):
    item_name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    requested_by = models.CharField(max_length=255)
    approval_status = models.CharField(
        max_length=20,
        choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')],
        default='Pending'
    )
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.item_name} - {self.approval_status}"

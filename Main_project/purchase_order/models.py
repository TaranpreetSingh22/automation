from django.db import models

class PurchaseOrder(models.Model):
    ref = models.CharField(max_length=255)
    date = models.DateField()
    to_address = models.TextField()
    instruments = models.CharField(max_length=255)
    quotation_no = models.CharField(max_length=255)
    quotation_date = models.DateField()
    branchname = models.CharField(max_length=255)
    terms = models.TextField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    total_gst = models.DecimalField(max_digits=10, decimal_places=2)
    pf = models.DecimalField(max_digits=10, decimal_places=2)
    grand_total_no_gst = models.DecimalField(max_digits=10, decimal_places=2)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2)
    pdf = models.FileField(upload_to='purchase_order_pdfs/', blank=True, null=True)

    def __str__(self):
        return f"Purchase Order {self.ref}"


class OrderItem(models.Model):
    purchase_order = models.ForeignKey(PurchaseOrder, related_name='items', on_delete=models.CASCADE)
    item_code = models.CharField(max_length=255)
    description = models.TextField()
    hsn_code = models.CharField(max_length=255)
    qty = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    gst_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    total_with_gst = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Item {self.item_code} for {self.purchase_order.ref}"

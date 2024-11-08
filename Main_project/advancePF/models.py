from django.db import models

class Vendor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ProcurementRequest(models.Model):
    description = models.TextField()
    vendors = models.ManyToManyField(Vendor, through='VendorQuote')

    def __str__(self):
        return self.description

class VendorQuote(models.Model):
    procurement_request = models.ForeignKey(ProcurementRequest, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    quote = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.vendor.name} - {self.quote}'

class AdvanceRequest(models.Model):
    from_user = models.CharField(max_length=100)
    date = models.DateField()
    invoice_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    amount_words = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    purpose = models.TextField()
    account_user = models.TextField()

    def __str__(self):
        return f'Advance Request from {self.from_user}'

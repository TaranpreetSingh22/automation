from django.db import models

class ProcurementRequest(models.Model):
    item = models.CharField(max_length=100)
    purpose = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    vendor = models.CharField(max_length=100)
    person_responsible = models.CharField(max_length=100)
    subject = models.CharField(max_length=200)
    date = models.DateField()
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.item} - {self.subject}"

# myapp/models.py
from django.db import models

class Purpose(models.Model):
    purpose = models.CharField(max_length=100)
    pdf_link = models.URLField()
    status = models.CharField(max_length=20)
    institutional_status = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.purpose


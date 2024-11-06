from django.db import models

# Create your models here.

class Vendor(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    gst_number = models.CharField(max_length=15)
    items = models.CharField(max_length=255)

    def _str_(self):
        return self.name
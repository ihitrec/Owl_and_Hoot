from django.db import models
import uuid

class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    products = models.JSONField()
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length= 31, null=True, blank=True)
    country = models.CharField(max_length= 40, null=False, blank=False)
    postcode = models.CharField(max_length= 20, null=True, blank=True)
    city = models.CharField(max_length= 40, null=False, blank=False)
    street_address1 = models.CharField(max_length= 80, null=False, blank=False)
    street_address2 = models.CharField(max_length= 80, null=True, blank=True)
    county = models.CharField(max_length= 80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, null=False)
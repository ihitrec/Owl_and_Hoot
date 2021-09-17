from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    sale_price = models.DecimalField(
        blank=True, null=True, max_digits=6, decimal_places=2)
    brand = models.CharField(blank=True, max_length=20)
    category = models.CharField(max_length=40)
    img = models.URLField()
    total_rating = models.DecimalField(
        default=0, max_digits=65, decimal_places=0)
    num_of_ratings = models.DecimalField(
        default=0, max_digits=65, decimal_places=0)
    rating = models.DecimalField(default=0, max_digits=3, decimal_places=2)
    gender = models.CharField(max_length=6)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

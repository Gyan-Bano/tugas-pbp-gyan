from django.utils import timezone
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    author = models.CharField(max_length=255)
    year = models.IntegerField()
    publisher = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    description = models.TextField()
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    amount = models.IntegerField()
    date_added = models.DateTimeField(default=timezone.now)  # Set a default value

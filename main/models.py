from django.db import models

# Create your models here.
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    image_url = models.URLField(blank=True, null=True)
    author = models.CharField(max_length=255)
    year = models.IntegerField()
    publisher = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    description = models.TextField()
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    amount = models.IntegerField()

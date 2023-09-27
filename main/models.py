from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal

class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    author = models.CharField(max_length=255)
    year = models.IntegerField()
    publisher = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    description = models.TextField()
    rating = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        validators=[
            MinValueValidator(Decimal('0.0'), message="Rating must be 0.0 or greater."),
            MaxValueValidator(Decimal('5.0'), message="Rating must be 5.0 or less."),
        ]
    )
    amount = models.IntegerField()
    date_added = models.DateTimeField(default=timezone.now)  # Set a default value
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal
from django.db.models.signals import pre_delete
from django.dispatch import receiver
import os

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
    date_added = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

@receiver(pre_delete, sender=Product)
def delete_product_image(sender, instance, **kwargs):
    # Get the image field value
    image = instance.image

    # Check if the image exists and delete it
    if image:
        if os.path.isfile(image.path):
            os.remove(image.path)

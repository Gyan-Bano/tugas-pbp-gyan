from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal
from django.db.models.signals import pre_delete
from django.dispatch import receiver
import os

class Product(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    author = models.CharField(max_length=255, null=True, blank=True, default='Default Author')
    year = models.IntegerField(null=True, blank=True, default=2023)
    publisher = models.CharField(max_length=255, null=True, blank=True, default='Default Publisher')
    genre = models.CharField(max_length=255, null=True, blank=True, default='Default Genre')
    description = models.TextField(null=True, blank=True)
    rating = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        validators=[
            MinValueValidator(Decimal('0.0'), message="Rating must be 0.0 or greater."),
            MaxValueValidator(Decimal('5.0'), message="Rating must be 5.0 or less."),
        ],
        null=True,
        blank=True,
        default=3.0  # Nilai default untuk rating
    )
    amount = models.IntegerField(null=True, blank=True)  # Nilai default untuk amount
    date_added = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def to_dict(self):
        product_dict = {
            'model': 'Product',
            'id': self.user.pk,
            'fields':{
                'name': self.name,
                'image': str(self.image),  # Convert ImageField to string for simplicity
                'author': self.author,
                'year': self.year,
                'publisher': self.publisher,
                'genre': self.genre,
                'description': self.description,
                'rating': float(self.rating),
                'amount': self.amount,
                'date_added': self.date_added.strftime("%Y-%m-%d %H:%M:%S"),  # Convert DateTimeField to string
                'user': self.user.pk if self.user else 0  # Get username if user exists
            }
        }
        return product_dict

@receiver(pre_delete, sender=Product)
def delete_product_image(sender, instance, **kwargs):
    # Get the image field value
    image = instance.image

    # Check if the image exists and delete it
    if image:
        if os.path.isfile(image.path):
            os.remove(image.path)

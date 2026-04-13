from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):
    CATEGORY_CHOICES = [
        ('ELEC', 'Electronics'),
        ('FASH', 'Fashion'),
        ('HOME', 'Home & Garden'),
        ('TOYS', 'Toys & Hobbies'),
        ('OTHR', 'Other'),
    ]
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    starting_bid = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='listing_images/', blank=True, null=True,default='listing_images/default.jpg')
    owner = models.ForeignKey(User, on_delete=models.CASCADE,related_name="owned_listings")
    category = models.CharField(max_length=4,choices=CATEGORY_CHOICES,default='OTHR')
    def __str__(self):
        return self.title
    

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):
    code = models.CharField(max_length=3)
    item = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.item} ({self.code})"


class bid(models.Model):
    item = models.ForeignKey(Listing, on_delete=models.CASCADE)
    bid = models.IntegerField()
    
    def __str__(self):
        return f"{self.item} {self.bid}"

class comment(models.Model):
    item = models.ForeignKey(Listing, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.item} {self.comment}"

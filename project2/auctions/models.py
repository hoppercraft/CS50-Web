from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):
    item = models.CharField(max_length=64)
    description = models.CharField(max_length=200)
    image = models.CharField(max_length=64)
    minimumbid = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.item} {self.description} {self.image} {self.minimumbid} {self.owner}"


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

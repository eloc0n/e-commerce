from django.conf import settings
from django.db import models
from datetime import datetime

from products.models import Laptop

# Create your models here.

class UserAddres(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.CharField(max_length=120)
    address2 = models.CharField(max_length=120, null=True, blank=True)
    city = models.CharField(max_length=120)
    country = models.CharField(max_length=120)
    zipcode = models.CharField(max_length=20)
    phone = models.CharField(max_length=120)
    message = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(default=datetime.now)
    

    def __str__(self):
        return "%s, %s, %s, %s, %s " %(self.address, self.city, self.country, self.zipcode, self.user.username)



class UserStripe(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    stripe_id = models.CharField(max_length=120)

    def __str__(self):
        return self.stripe_id


class UserFavourite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
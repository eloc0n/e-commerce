from django.contrib import admin
from .models import UserAddres, UserStripe, UserFavourite

# Register your models here.
admin.site.register(UserAddres)
admin.site.register(UserStripe)
admin.site.register(UserFavourite)
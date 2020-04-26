from django.contrib import admin
from .models import UserAddres, UserStripe

# Register your models here.
admin.site.register(UserAddres)
admin.site.register(UserStripe)
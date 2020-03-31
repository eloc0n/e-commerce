from django.db import models

from datetime import datetime

# Create your models here.

STORAGE_TYPE_CHOICES = (
    ('HDD', 'HDD'),
    ('SSD', 'SSD'),
    ('NVMe', 'NVMe'),
    )

SCREEN_SIZE_CHOICES = (
    ('14', '14'),
    ('15.6', '15.6'),
    ('17', '17'),
)

SCREEN_RESOLUTION_CHOICES = (
    ('768', '768'), 
    ('1080', '1080'), 
    ('1440', '1440'), 
)

SCREEN_PANEL_CHOICES = (
    ('TN', 'TN'),
    ('VA', 'VA'),
    ('IPS', 'IPS'),
)

REFRESH_CHOICES = (
    ('60', '60'),
    ('120', '120'),
    ('144', '144'),
)

RAM_CHOICES = (
    ('8', '8'),
    ('16', '16'),
    ('32', '32'),
)



class Laptop(models.Model):
    # product_id
    title = models.CharField(max_length=120)
    operating_system = models.CharField(max_length=20, default='Win 10')
    manufacturer = models.CharField(max_length=120)
    cpu = models.CharField(max_length=120)
    cores = models.IntegerField()
    threads = models.IntegerField()
    storage = models.IntegerField()
    storage_type = models.CharField(max_length=20, choices=STORAGE_TYPE_CHOICES)
    screen_size = models.CharField(max_length=20, choices=SCREEN_SIZE_CHOICES)
    screen_resolution = models.CharField(max_length=20, choices=SCREEN_RESOLUTION_CHOICES)
    screen_panel = models.CharField(max_length=20, choices=SCREEN_PANEL_CHOICES)
    refresh = models.CharField(max_length=20, choices=REFRESH_CHOICES)
    ram = models.CharField(max_length=20, choices=RAM_CHOICES)
    ram_type = models.CharField(max_length=20, default='DDR4')
    gpu = models.CharField(max_length=120)
    gpu_ram = models.IntegerField()
    description = models.TextField()
    price = models.DecimalField(max_digits=1000, decimal_places=2)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    active = models.BooleanField(default=True)
    date = models.DateTimeField(default=datetime.now, blank=True)
    bestseller = models.BooleanField(default=False)

    def __str__(self):
        return self.title
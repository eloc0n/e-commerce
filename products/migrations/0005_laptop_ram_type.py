# Generated by Django 3.0.4 on 2020-03-31 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_laptop_operating_system'),
    ]

    operations = [
        migrations.AddField(
            model_name='laptop',
            name='ram_type',
            field=models.CharField(default='DDR4', max_length=20),
        ),
    ]

# Generated by Django 3.0.4 on 2020-05-02 09:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20200402_1448'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0003_userstripe'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserFavourite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('laptop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Laptop')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

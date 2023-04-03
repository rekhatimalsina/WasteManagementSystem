# Generated by Django 4.1.7 on 2023-03-31 02:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterVehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_no', models.CharField(default=0, max_length=50, unique=True)),
                ('vehicle_type', models.CharField(default=0, max_length=50)),
                ('driver_name', models.CharField(default=0, max_length=50)),
                ('driver_photo', models.ImageField(blank=True, null=True, upload_to='static/images/')),
                ('driver_license_no', models.CharField(default=0, max_length=50, unique=True)),
                ('license_photo', models.ImageField(blank=True, null=True, upload_to='static/images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
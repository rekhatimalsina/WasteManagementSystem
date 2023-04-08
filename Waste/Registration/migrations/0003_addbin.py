# Generated by Django 4.1 on 2023-04-08 07:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DriverRegistration', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Registration', '0002_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddBin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=0, max_length=50)),
                ('garbage_type', models.CharField(default=0, max_length=50, null=0)),
                ('garbage_image', models.ImageField(blank=True, null=True, upload_to='static/images/')),
                ('area', models.CharField(default=0, max_length=50, null=0)),
                ('latitude', models.CharField(default=0, max_length=50, null=0)),
                ('longitude', models.CharField(default=0, max_length=50, null=0)),
                ('amount', models.CharField(default=0, max_length=100, null=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DriverRegistration.registervehicle')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

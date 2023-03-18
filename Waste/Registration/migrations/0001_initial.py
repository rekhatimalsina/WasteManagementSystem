# Generated by Django 4.1.6 on 2023-03-18 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(default=0, max_length=50, null=0)),
                ('full_name', models.CharField(default=0, max_length=50, null=0)),
                ('dob', models.DateField(max_length=20)),
                ('password', models.CharField(default=0, max_length=50, null=0)),
                ('confirm_password', models.CharField(default=0, max_length=50, null=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
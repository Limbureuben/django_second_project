# Generated by Django 5.1.2 on 2024-10-20 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_files_weather'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.DeleteModel(
            name='Weather',
        ),
    ]
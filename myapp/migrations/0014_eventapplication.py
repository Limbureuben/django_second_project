# Generated by Django 5.1.2 on 2024-10-30 14:46

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_remove_event_created_by_remove_event_is_public_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('status', models.CharField(choices=[('attending', 'Attending'), ('not_attending', 'Not Attending'), ('interested', 'Interested')], max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='myapp.event')),
            ],
        ),
    ]
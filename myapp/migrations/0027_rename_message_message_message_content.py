# Generated by Django 5.1.2 on 2024-12-21 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0026_message_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='message',
            new_name='message_content',
        ),
    ]

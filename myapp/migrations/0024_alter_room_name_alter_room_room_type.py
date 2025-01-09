# Generated by Django 5.1.2 on 2024-12-16 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0023_room_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='name',
            field=models.CharField(choices=[('Small', 'Small Room (1-20 people)'), ('Small 2 ', 'Small Room (21-50 people)'), ('Medium', ' Medium Room (51-100 people)'), ('Medium 2', 'Medium Room (101-150 people)'), ('Large ', 'Large Room (151-200 people)'), ('Large 2', 'Large Room (201-300 people)')], max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_type',
            field=models.CharField(choices=[('Small', 'Small Room (1-20 people)'), ('Small 2 ', 'Small Room (21-50 people)'), ('Medium', ' Medium Room (51-100 people)'), ('Medium 2', 'Medium Room (101-150 people)'), ('Large ', 'Large Room (151-200 people)'), ('Large 2', 'Large Room (201-300 people)')], max_length=20),
        ),
    ]

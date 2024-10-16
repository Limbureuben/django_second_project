from django.db import models
from datetime import date
import uuid
from django.contrib.auth.models import AbstractUser
from pyexpat import model


# Create your models here.

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255, default="",)
    last_name = models.CharField(max_length=255, default="")
    course = models.CharField(max_length=255, default="")
    registration_number = models.CharField(max_length=255, default="")
    registration_date = models.DateField(default=date.today)
    

class Weather(models.Model):
    temperature = models.FloatField()
    humidity = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    
class Files(models.Model):
    file = models.FileField(upload_to="uploads/", null=True, blank=True)
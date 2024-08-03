from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=50)
    college=models.CharField(max_length=50)
    age=models.CharField(max_length=10)
    isActive=models.BooleanField(default=False)
    
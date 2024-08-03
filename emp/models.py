from django.db import models

# Create your models here.
class emp(models.Model):
    name=models.CharField(max_length=50)
    eid=models.CharField(max_length=20,primary_key=True)
    phone=models.CharField(max_length=10)
    working=models.BooleanField(default=False)
    department=models.CharField(max_length=10)
    address=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    
class Testimonial(models.Model):
    name=models.CharField(max_length=20)
    desc=models.TextField(max_length=100)
    file=models.FileField(upload_to='testimonials/')
    rating=models.IntegerField(blank=True,null=True)

    def __str__(self) -> str:
        return self.name

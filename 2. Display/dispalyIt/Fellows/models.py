from django.db import models

# Create your models here.
class MyFellows(models.Model):
    name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

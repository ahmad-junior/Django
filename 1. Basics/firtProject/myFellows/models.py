from django.db import models

# Create your models here.
class MyFellows(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=25)
    zip = models.CharField(max_length=10)
    country = models.CharField(max_length=20)
    notes = models.CharField(max_length=200)
    def __str__(self):
        return self.name
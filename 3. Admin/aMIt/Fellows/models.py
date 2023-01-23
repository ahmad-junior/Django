from django.db import models
from django.contrib import admin

# Create your models here.
class Fellow(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    birth_date = models.DateField()
    
    def __str__(self):
        return self.first_name + " " + self.last_name

# Create list_display for FellowAdmin
class FellowAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "phone", "address", "city", "state", "country", "birth_date")
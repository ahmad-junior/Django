from django.db import models

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=13)
    
    def __str__(self):
        return self.name
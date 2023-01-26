from django.db import models

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    contact = models.CharField(max_length=11)

    def __str__(self):
        return self.name
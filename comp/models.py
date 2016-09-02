from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField("好的",max_length=30)
    address = models.CharField(max_length=50)

        

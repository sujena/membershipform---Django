from django.db import models

# Create your models here.

class Member(models.Model):
    name= models.CharField(max_length=100)
    email= models.EmailField(max_length=254)
    address = models.CharField(max_length=100)
    phone= models.CharField(max_length=20)
    date= models.DateTimeField(auto_now_add=True)

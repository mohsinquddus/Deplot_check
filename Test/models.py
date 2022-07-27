from django.db import models
from django.utils import timezone

# Create your models here.

class Genre(models.Model):
    genree = models.CharField(max_length=256)

    def __str__(self):
        return self.genree
    
class Movies(models.Model):
    title = models.CharField(max_length=256)
    year = models.IntegerField()
    stock = models.IntegerField()
    duration = models.IntegerField()
    created_date = models.DateField(default=timezone.now)
    genre = models.ForeignKey(Genre, default='Mohsin', on_delete=models.CASCADE)
    

class Contacts(models.Model):
    name = models.CharField(max_length=250)
    phone = models.CharField(max_length=250) 
    email = models.CharField(max_length=250) 
    desc = models.TextField(max_length=50) 
    date = models.DateTimeField(auto_now=False, auto_now_add=False) 

    def __str__(self):
        return self.name
from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=100) 
    price = models.IntegerField(default=100)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.name
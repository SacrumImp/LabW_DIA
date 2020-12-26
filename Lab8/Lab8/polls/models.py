from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=200)
    population = models.IntegerField()
    area = models.IntegerField()
    image = models.ImageField()
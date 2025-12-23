from django.db import models

# Create your models here.
# Gives the structure for fields in database

class Phones(models.Model):

    name = models.CharField(max_length = 30, blank = False)
    color = models.CharField(max_length = 30, blank = False)
    price = models.IntegerField (default = 0)

    def __str__(self):
        return self.name

class MainSpec(models.Model):

    name = models.CharField(max_length = 255)
    property = models.CharField(max_length = 255)

    def __str__(self):
        return self.name
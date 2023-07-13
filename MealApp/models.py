from django.db import models


class Meal(models.Model):
    name = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100)
    cookTime = models.IntegerField()
    cost = models.FloatField()


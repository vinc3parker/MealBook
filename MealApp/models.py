from django.db import models


class Ingredient(models.Model):
    CATEGORY_CHOICES = [
        ('meat', 'Meat'),
        ('vegetable', 'Vegetable'),
        ('fruit', 'Fruit'),
        ('eggs', 'Eggs'),
        ('dairy', 'Dairy'),
        ('fats_oils', 'Fats and Oils'),
        ('baking', 'Baking Products'),
        ('herbs_spices', 'Herbs and Spices'),
        ('pasta', 'Pasta'),
        ('rice', 'Rice'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, null=True)
    protein_per_100g = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    kcal_per_100g = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    carbs_per_100g = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)

    def __str__(self):
        return self.name


class Meal(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default='Tasty Meal!')
    instructions = models.TextField(default='Instructions seem to have been misplaced ')
    ingredients = models.ManyToManyField(Ingredient)
    cook_time = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Cookbook(models.Model):
    name = models.CharField(max_length=100)
    meals = models.ManyToManyField(Meal)

    def __str__(self):
        return self.name

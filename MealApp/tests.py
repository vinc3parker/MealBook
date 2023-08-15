from django.test import TestCase
from django.urls import reverse
from .models import Ingredient, Meal, Cookbook

# Create your tests here.
class IngredientModelTest(TestCase):
    def setUp(self):
        Ingredient.objects.create(name="Eggs", category="Protein")

    def test_ingredient_str(self):
        ingredient = Ingredient.objects.get(name="Eggs")
        self.assertEqual(str(ingredient), "Eggs")

    def test_ingredient_category_choices(self):
        ingredient = Ingredient.objects.get(name="Eggs")
        category_choices = ingredient._meta.get_field("category").choices
        self.assertIn(("Protein", "Protein"), category_choices)
        self.assertIn(("Vegetable", "Vegetable"), category_choices)

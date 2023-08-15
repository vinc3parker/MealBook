from django.urls import path
from . import views

urlpatterns = [
    # ex: /mealbook/contact/
    path('contact/', views.contact, name='contact'),
    # ex: /mealbook/cookbook/edit/****
    path('cookbook/edit/<int:pk>/', views.CookbookUpdateView.as_view(), name='edit_cookbook'),
    # ex: /mealbook/cookbook/delete/****
    path('cookbook/delete/<int:pk>/', views.CookbookDeleteView.as_view(), name='delete_cookbook'),
    # ex: /mealbook/meal/edit/****
    path('meal/edit/<int:pk>/', views.MealUpdateView.as_view(), name='edit_meal'),
    # ex: /mealbook/meal/delete/****
    path('meal/delete/<int:pk>/', views.MealDeleteView.as_view(), name='delete_meal'),
    # ex: /mealbookk/ingredient/edit/****
    path('ingredient/edit/<int:pk>/', views.IngredientUpdateView.as_view(), name='edit_ingredient'),
    # ex: /mealbook/ingredient/delete/****
    path('ingredient/delete/<int:pk>/', views.IngredientDeleteView.as_view(), name='delete_ingredient'),
    # ex: /mealbook/addCookbook
    path('addCookbook/', views.add_cookbook, name='addCookbook'),
    # ex: /mealbook/addMeal
    path('addMeal/', views.add_meal, name='addMeal'),
    # ex: /mealbook/addIngredient
    path('addIngredient/', views.add_ingredient, name='addIngredient'),
    # ex: /mealbook/
    path('', views.home, name='home'),
    # ex: /mealbook/cookbook
    path('cookbook/', views.cookbook, name='cookbook'),
    # ex: /mealbook/cookbooks
    path('cookbooks/', views.cookbooks, name='cookbooks'),
    # ex: /mealbook/meals
    path('meals/', views.meals, name='meals'),
    # ex: /mealbook/ingredients
    path('ingredients/', views.ingredients, name='ingredients'),
]

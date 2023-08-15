from django.core.management.base import BaseCommand
from mealapp.models import Meal, Ingredient, Cookbook, User

class Command(BaseCommand):
    def handle(self, *args, **options):
        # Clear all existing meal objects from the database
        Meal.objects.all().delete()

        # Create 15 new meal objects and save them to the database
        meals = [
            {
                'name': 'Spaghetti Bolognese',
                'description': 'Classic Italian pasta dish with meat sauce',
                'ingredients': 'Spaghetti, ground beef, tomatoes, onions, garlic, herbs',
                'instructions': 'Cook spaghetti. Brown beef with onions and garlic. Add tomatoes and herbs. Simmer and serve.',
                'cook_time': 30,
            },
            {
                'name': 'Chicken Stir-Fry',
                'description': 'A delicious mix of chicken and vegetables',
                'ingredients': 'Chicken breast, bell peppers, broccoli, carrots, soy sauce, ginger',
                'instructions': 'Stir-fry chicken and vegetables in soy sauce and ginger. Serve over rice.',
                'cook_time': 40,
            },
            {
                'name': 'Vegetarian Pizza',
                'description': 'Delicious pizza with various vegetables',
                'ingredients': 'Pizza dough, tomato sauce, mozzarella cheese, bell peppers, mushrooms, olives',
                'instructions': 'Spread sauce on dough. Add cheese and vegetables. Bake until crust is crispy.',
                'cook_time': 25
            },
            {
                'name': 'Grilled Salmon',
                'description': 'Healthy grilled salmon with lemon',
                'ingredients': 'Salmon fillet, lemon, olive oil, salt, pepper',
                'instructions': 'Season salmon with oil, salt, and pepper. Grill until cooked. Squeeze lemon on top.',
                'cook_time': 30
            },
            {
                'name': 'Mushroom Risotto',
                'description': 'Creamy rice dish with mushrooms',
                'ingredients': 'Arborio rice, mushrooms, onion, garlic, vegetable broth, parmesan cheese',
                'instructions': 'Saute mushrooms, onion, and garlic. Add rice and broth. Stir until creamy. Add cheese.',
                'cook_time': 30
            },
            # Add more meal objects
            {
                'name': 'Beef Stew',
                'description': 'Hearty beef stew with vegetables',
                'ingredients': 'Beef chuck, potatoes, carrots, onions, beef broth, tomato paste',
                'instructions': 'Brown beef. Add vegetables, broth, and tomato paste. Simmer until tender.',
                'cook_time': 45
            },
            {
                'name': 'Chicken Alfredo',
                'description': 'Creamy pasta dish with chicken and Alfredo sauce',
                'ingredients': 'Chicken breast, fettuccine, heavy cream, butter, parmesan cheese',
                'instructions': 'Cook chicken. Prepare Alfredo sauce. Toss with cooked pasta and chicken.',
                'cook_time': 35
            },
            {
                'name': 'Greek Salad',
                'description': 'Fresh and healthy Greek salad',
                'ingredients': 'Cucumbers, tomatoes, olives, feta cheese, red onions, olive oil, lemon juice',
                'instructions': 'Chop vegetables. Add olives and feta. Drizzle with olive oil and lemon juice.',
                'cook_time': 20
            },
            {
                'name': 'Lemon Herb Roasted Chicken',
                'description': 'Roasted chicken with lemon and herbs',
                'ingredients': 'Whole chicken, lemon, thyme, rosemary, garlic, olive oil',
                'instructions': 'Season chicken with herbs and lemon. Roast until golden and cooked through.',
                'cook_time': 30
            },
            {
                'name': 'Pasta Carbonara',
                'description': 'Italian pasta with eggs, cheese, and bacon',
                'ingredients': 'Spaghetti, eggs, parmesan cheese, bacon, black pepper',
                'instructions': 'Cook spaghetti. Mix eggs, cheese, and cooked bacon. Toss with hot pasta.',
                'cook_time': 25
            },
            # Add more meal objects
            {
                'name': 'Shrimp Scampi',
                'description': 'Garlicky shrimp with butter and wine sauce',
                'ingredients': 'Shrimp, garlic, butter, white wine, lemon juice, parsley',
                'instructions': 'Saute shrimp and garlic in butter. Add wine and lemon. Serve over pasta.',
                'cook_time': 30
            },
            {
                'name': 'Vegetable Stir-Fry',
                'description': 'Healthy mix of assorted vegetables',
                'ingredients': 'Broccoli, bell peppers, carrots, snow peas, soy sauce, sesame oil',
                'instructions': 'Stir-fry vegetables in sesame oil and soy sauce. Serve over rice or noodles.',
                'coo_time': 25
            },
            {
                'name': 'Taco Salad',
                'description': 'Tasty salad with taco-seasoned meat and toppings',
                'ingredients': 'Ground beef, lettuce, tomatoes, cheese, tortilla chips, salsa',
                'instructions': 'Cook ground beef with taco seasoning. Assemble salad with toppings.',
                'cook_time': 15
            },
            {
                'name': 'Egg Fried Rice',
                'description': 'Classic Chinese fried rice with eggs',
                'ingredients': 'Cooked rice, eggs, vegetables, soy sauce, sesame oil',
                'instructions': 'Scramble eggs. Stir-fry rice and vegetables. Mix with eggs and sauce.',
                'cook_time': 25
            },
            {
                'name': 'Caprese Salad',
                'description': 'Simple Italian salad with tomatoes, mozzarella, and basil',
                'ingredients': 'Tomatoes, fresh mozzarella, basil leaves, balsamic glaze',
                'instructions': 'Arrange tomatoes, mozzarella, and basil. Drizzle with balsamic glaze.',
                'cook_time': 20
            },
        ]

        for meal_data in meals:
            meal = Meal.objects.create(
                name=meal_data['name'],
                description=meal_data['description'],
                ingredients=meal_data['ingredients'],
                instructions=meal_data['instructions'],
            )
            self.stdout.write(f'Successfully created meal: {meal.name}')

        self.stdout.write(self.style.SUCCESS('Successfully seeded database with 15 meals.'))

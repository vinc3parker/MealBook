from django.shortcuts import render, redirect
from .forms import IngredientForm, MealForm, CookbookForm, ContactForm
from .models import Ingredient, Meal, Cookbook
from django.views.generic.edit import UpdateView, DeleteView


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            send_mail(
                subject,
                message,
                email,
                ['your_site_owner_email@example.com'],  # Replace with actual email
                fail_silently=False,
            )

            return HttpResponseRedirect(reverse('contact'))  # Redirect to contact page after submission

    else:
        form = ContactForm()

    return render(request, 'mealapp/contact.html', {'form': form})


def home(request):
    context = {}
    return render(request, 'mealapp/home.html', context)


def cookbook(request):
    context = {}
    return render(request, 'mealapp/cookbook.html', context)


def cookbooks(request):
    cookbooks = Cookbook.objects.all()  # Retrieve all meals from the database
    context = {'cookbooks': cookbooks}
    return render(request, 'mealapp/cookbooks.html', context)


def add_cookbook(request):
    if request.method == 'POST':
        form = CookbookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cookbooks')  # Redirect back to the cookbooks page
    else:
        form = CookbookForm()
    return render(request, 'mealapp/add_cookbook.html', {'form': form})


class CookbookUpdateView(UpdateView):
    model = Cookbook
    form_class = CookbookForm
    template_name = 'mealapp/edit_cookbook.html'

    def form_valid(self, form):
        form.save()
        return redirect('cookbooks')


class CookbookDeleteView(DeleteView):
    model = Cookbook
    template_name = 'mealapp/cookbook_confirm_delete.html'
    success_url = '/mealbook/cookbooks'


def meals(request):
    meals = Meal.objects.all()  # Retrieve all meals from the database
    context = {'meals': meals}  # Pass the meals queryset to the context
    return render(request, 'mealapp/meals.html', context)


def add_meal(request):
    if request.method == 'POST':
        form = MealForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('meals')  # Redirect back to the meals page
    else:
        form = MealForm()
    return render(request, 'mealapp/add_meal.html', {'form': form})


class MealUpdateView(UpdateView):
    model = Meal
    fields = ['name', 'category', 'ingredients']
    template_name = 'mealapp/meal_form.html'

    def form_valid(self, form):
        form.save()
        return redirect('meals')


class MealDeleteView(DeleteView):
    model = Meal
    template_name = 'mealapp/meal_confirm_delete.html'
    success_url = '/mealbook/meals'


def ingredients(request):
    ingredients = Ingredient.objects.all()  # Retrieve all ingredients from the database
    context = {'ingredients': ingredients}  # Pass the ingredients queryset to the context
    return render(request, 'mealapp/ingredients.html', context)


def add_ingredient(request):
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ingredients')  # Redirect back to the ingredients page
    else:
        form = IngredientForm()
    return render(request, 'mealapp/add_ingredient.html', {'form': form})


class IngredientUpdateView(UpdateView):
    model = Ingredient
    form_class = IngredientForm  # Use the same form for editing
    template_name = 'mealapp/edit_ingredient.html'  # Create this template

    def form_valid(self, form):
        form.save()
        return redirect('ingredients')  # Redirect to ingredients list after edit


class IngredientDeleteView(DeleteView):
    model = Ingredient
    template_name = 'mealapp/delete_ingredient.html'  # Create this template
    success_url = '/mealbook/ingredients'  # Redirect to ingredients list after delete

from django.shortcuts import render, redirect
from mealapp.models import Meal
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages


def home(request):
    meals = Meal.objects.all()
    context = {'meals': meals}
    return render(request, 'mealapp/home.html', context)


def about(request):
    context = {}
    return render(request, 'mealapp/about.html', context)


def cookbook(request):
    context = {}
    return render(request, 'mealapp/cookbook.html', context)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mealbook/login')
        else:
            print("Form erroros:", form.errors)
    else:
        form = UserCreationForm()
    return render(request, 'mealapp/signup.html', {'form': form})


def login(request):
    if request.method == 'POST':
        # Perform login authentication and processing here
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                # If the user is valid, log them in and redirect to a specific page
                login(request, user)
                return redirect('home')  # Replace 'home' with the appropriate URL name for the home page
            else:
                # If the user is not valid or login fails, handle the error (e.g., show an error message)
                # For simplicity, we'll just return the login page again in this example
                return render(request, 'mealapp/login.html', {'form': form})

    else:
        # If the request method is not POST (e.g., GET request), render the login page with an empty form
        form = AuthenticationForm()

    return render(request, 'mealapp/login.html', {'form': form})


def profile(request):
    user = request.user
    return render(request, 'mealapp/profile.html', {'user': user})


def perform_logout(request):
    if request.method == 'POST':
        logout(request)  # Logout the user
        messages.success(request, 'You have been successfully logged out.')
        return redirect('home')  # Redirect to the home page after logout

    # Render the logout template for GET requests
    return render(request, 'mealapp/logout.html')
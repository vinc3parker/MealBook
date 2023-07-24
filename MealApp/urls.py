from django.urls import path
from . import views

urlpatterns = [
    # ex: /mealbook/
    path('', views.home, name='home'),
    # ex: /mealbook/about
    path('about/', views.about, name='about'),
    # ex: /mealbook/cookbook
    path('cookbook/', views.cookbook, name='cookbook'),
    # ex: /mealbook/signup/
    path('signup/', views.signup, name='signup'),
    # ex: /mealbook/login
    path('login/', views.login, name='login'),
    #ex: /mealbook/profile
    path('profile/', views.profile, name='profile'),
    #ex: /mealbook/logout
    path('logout/', views.perform_logout, name='logout'),
]

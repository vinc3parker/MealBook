from django import forms
from .models import Ingredient, Meal, Cookbook


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = '__all__'


class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = '__all__'
        widgets = {
            'ingredients': forms.CheckboxSelectMultiple,  # Use CheckboxSelectMultiple widget
        }


class CookbookForm(forms.ModelForm):
    class Meta:
        model = Cookbook
        fields = '__all__'
        widgets = {
            'meals': forms.CheckboxSelectMultiple,  # Use CheckboxSelectMultiple widget
        }


class ContactForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100)
    email = forms.EmailField(label='Your Email')
    subject = forms.CharField(label='Subject', max_length=200)
    message = forms.CharField(label='Message', widget=forms.Textarea)

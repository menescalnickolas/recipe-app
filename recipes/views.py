from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Recipes
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def home (request):
  return render(request, 'recipes/recipes_home.html')

class RecipesListView(LoginRequiredMixin, ListView):
  model = Recipes
  template_name = 'recipes/main.html'

class RecipeDetailView(LoginRequiredMixin, DetailView):
  model = Recipes
  template_name = 'recipes/detail.html'
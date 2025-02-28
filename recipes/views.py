from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Recipes
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RecipesSearchForm
from .models import Recipes
import pandas as pd

# Create your views here.
def home (request):
  return render(request, 'recipes/recipes_home.html')

class RecipesListView(LoginRequiredMixin, ListView):
  model = Recipes
  template_name = 'recipes/main.html'
  context_object_name = 'recipes'
  form_class = RecipesSearchForm

  def get_queryset(self):
    queryset = Recipes.objects.all() # Fetch all recipes initially
    self.form = self.form_class(self.request.GET or None) # Get form data
    self.recipes_df = None  # Initialize empty data for template

    if self.request.GET and self.form.is_valid():
      recipe_name = self.request.GET.get('recipe_name')
      chart_type = self.request.GET.get('chart_type')

      if recipe_name:
        queryset = queryset.filter(name__icontains=recipe_name) # Case-insensitive search

      if queryset.exists():
        self.recipes_df = pd.DataFrame(queryset.values()).to_html()
      
      return queryset
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['form'] = self.form  # Ensure form is passed to the template
    context['recipes_df'] = self.recipes_df  # Include filtered results (if any)
    return context

class RecipeDetailView(LoginRequiredMixin, DetailView):
  model = Recipes
  template_name = 'recipes/detail.html'
  
















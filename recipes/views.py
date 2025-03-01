from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Recipes
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RecipesSearchForm
from .models import Recipes
import pandas as pd
from .utils import get_recipename_from_id, get_chart

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
    self.chart = None

    chart_type = self.request.GET.get('chart_type', '#2')
    
  
    if self.request.GET and self.form.is_valid():
      search_query = self.request.GET.get('search_query', '')
      chart_type = self.request.GET.get('chart_type', '')

      print(search_query, chart_type)

      print('Exploring querysets:')
      print ('Case 1: Output of Sale.objects.all()')
      qs = Recipes.objects.all()
      print(qs)

      print('Case 2: Output of Sale.objects.filter(book_name=book_title)')
      qs = Recipes.objects.filter(name__icontains=search_query)
      if qs:
        recipes_df=pd.DataFrame(qs.values())
        recipes_df['recipe_id']=recipes_df['recipe_id'].apply(get_recipename_from_id)
        
        recipes_df = recipes_df.to_html()
      print(qs)

      print('Case 3: Output of qs.values')
      print(qs.values_list())

      print('Case 5: Output of Sale.objects.get(id=1)')
      obj = Recipes.objects.get(id=1)
      print(obj)

      if search_query:
        queryset = queryset.filter(
          name__icontains=search_query
          ) | queryset.filter(
            cooking_time__icontains=search_query
            ) | queryset.filter(
              ingredients__icontains=search_query
              ) | queryset.filter(
                difficulty__icontains=search_query
                )
      
      self.chart = get_chart(chart_type, queryset)

      if queryset.exists():
        self.recipes_df = pd.DataFrame(queryset.values()).to_html()
      
    return queryset
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['form'] = self.form  # Ensure form is passed to the template
    context['recipes_df'] = self.recipes_df  # Include filtered results (if any)
    

    if self.chart is None:
      self.chart = get_chart('#2', Recipes.objects.all())
    
    context['chart'] = self.chart  
      
    return context

class RecipeDetailView(LoginRequiredMixin, DetailView):
  model = Recipes
  template_name = 'recipes/detail.html'
  
















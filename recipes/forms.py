from django import forms
from .models import Recipes


CHART__CHOICES = (
  ('#1', 'Bar Chart'),
  ('#2', 'Pie chart'),
  ('#3', 'Line chart')
)

class RecipesSearchForm(forms.Form):
  search_query = forms.CharField(required=False, label="Search recipes, ingredients, difficulty, cooking time...")
  chart_type = forms.ChoiceField(choices=CHART__CHOICES)

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipes
        fields = ['name', 'description', 'cooking_time', 'ingredients', 'preparation_method', 'pic']

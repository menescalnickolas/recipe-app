from django import forms

CHART__CHOICES = (
  ('#1', 'Bar Chart'),
  ('#2', 'Pie chart'),
  ('#3', 'Line chart')
)

class RecipesSearchForm(forms.Form):
  search_query = forms.CharField(required=False, label="Search recipes, ingredients, difficulty, cooking time...")
  chart_type = forms.ChoiceField(choices=CHART__CHOICES)


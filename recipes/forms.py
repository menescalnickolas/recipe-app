from django import forms

CHART__CHOICES = (
  ('#1', 'Bar Chart'),
  ('#2', 'Pie chart'),
  ('#3', 'Line chart')
)

class RecipesSearchForm(forms.Form):
  recipe_name = forms.CharField(max_length=120)
  chart_type = forms.ChoiceField(choices=CHART__CHOICES)


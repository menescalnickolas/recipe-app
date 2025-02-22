from django.test import TestCase
from .models import Recipes
from django.urls import reverse

# Create your tests here.
class RecipesModelTest(TestCase):
  def setUpTestData():
    Recipes.objects.create(recipe_id=1, name="Brigadeiro", cooking_time=15, ingredients="Condensed milk, cocoa powder")

  def test_recipe_name(self):
    recipe = Recipes.objects.get(recipe_id=1)
    field_label = recipe._meta.get_field('name').verbose_name
    self.assertEqual(field_label, 'name')

  def test_cooking_time(self):
    recipe = Recipes.objects.get(recipe_id=1)
    self.assertEqual(recipe.cooking_time, 15)

  def test_difficulty_easy(self):
    recipe = Recipes.objects.get(recipe_id=1)
    self.assertEqual(recipe.difficulty, "Intermediate")

class RecipesListViewTest(TestCase):
    def setUpTestData():
        Recipes.objects.create(name="Brigadeiro", cooking_time=15, ingredients="Condensed milk, cocoa powder")
        Recipes.objects.create(name="Pasta", cooking_time=20, ingredients="Pasta, tomato sauce")

    def test_recipe_list_page(self):
        response = self.client.get(reverse('/list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipes/main.html')

    def test_recipe_detail_links(self):
        recipes = Recipes.objects.all()
        for recipe in recipes:
            response = self.client.get(reverse('/list', args=[recipe.recipe_id]))  # Adjust the URL pattern if needed
            self.assertEqual(response.status_code, 200)
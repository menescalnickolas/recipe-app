from django.test import TestCase
from .models import Recipes

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

  def test_recipe_list_page(self):
    response = self.client.get('/list/')
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'recipes/main.html')

  def test_recipe_detail_links(self):
    Recipes.objects.create(recipe_id=1, name="Brigadeiro", cooking_time=15, ingredients="Condensed milk, cocoa powder")
    response = self.client.get('/list/1')
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, "recipes/detail.html")
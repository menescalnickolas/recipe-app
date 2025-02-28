from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .models import Recipes


# Create your tests here.
class RecipesModelTest(TestCase):
  @classmethod
  def setUpTestData(cls):
    cls.user = User.objects.create_user(username='testuser', password='testpassword')

    Recipes.objects.create(recipe_id=1, name="Brigadeiro", cooking_time=15, ingredients="Condensed milk, cocoa powder")

  def test_recipe_name(self):
    recipe = Recipes.objects.get(recipe_id=1)
    field_label = recipe._meta.get_field('name').verbose_name
    self.assertEqual(field_label, 'name')

  def test_cooking_time(self):
    recipe = Recipes.objects.get(recipe_id=1)
    self.assertEqual(recipe.cooking_time, 15)

  def test_ingredients_format(self):
    recipe = Recipes.objects.get(recipe_id=1)
    ingredients = recipe.ingredients.split(',')
    self.assertEqual(len(ingredients), 2)

  def test_difficulty_easy(self):
    recipe = Recipes.objects.get(recipe_id=1)
    self.assertEqual(recipe.difficulty, "Intermediate")

  def test_recipe_list_page(self):
    self.client.login(username='testuser', password='testpassword')
    response = self.client.get(reverse('recipes:list'))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'recipes/main.html')

  def test_recipe_detail_links(self):
    self.client.login(username='testuser', password='testpassword')
    Recipes.objects.create(recipe_id=1, name="Brigadeiro", cooking_time=15, ingredients="Condensed milk, cocoa powder")
    response = self.client.get(reverse('recipes:detail', args=[1]))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, "recipes/detail.html")

  def test_search_functionality(self):
    self.client.login(username='testuser', password='testpassword')
    response = self.client.get(reverse('recipes:list') + '?search_query=Brigadeiro')
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, "Brigadeiro")

  def test_recipe_list_view_authenticated(self):
    self.client.login(username='testuser', password='testpassword')
    response = self.client.get(reverse('recipes:list'))
    self.assertEqual(response.status_code, 200)

  def test_login_required_for_recipe_main_page(self):
    self.client.login(username='testuser', password='testpassword')
    response = self.client.get(reverse('recipes:list'))
    self.assertEqual(response.status_code, 200)
  
  
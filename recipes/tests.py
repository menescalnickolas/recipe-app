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

class RecipesViewsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='testpassword')
        cls.recipe = Recipes.objects.create(
            recipe_id=1,
            name="Brigadeiro",
            cooking_time=15,
            ingredients="Condensed milk, cocoa powder",
            difficulty="Intermediate"
        )

    def test_recipe_list_page(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('recipes:list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipes/main.html')

    def test_recipe_detail_page(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('recipes:detail', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "recipes/detail.html")

    def test_search_functionality(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('recipes:list') + '?search_query=Brigadeiro')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Brigadeiro")

    def test_recipe_list_requires_login(self):
        response = self.client.get(reverse('recipes:list'))
        self.assertNotEqual(response.status_code, 200)  # Should redirect to login page

    def test_recipe_creation(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('recipes:add'), {
            'name': 'Pão de Queijo',
            'description': 'Test',
            'cooking_time': 30,
            'preparation_method': 'Test',
            'ingredients': 'Tapioca flour, cheese, eggs',
        })
        self.assertEqual(response.status_code, 302)  # Should redirect after creation
        self.assertTrue(Recipes.objects.filter(name='Pão de Queijo').exists())

    def test_invalid_recipe_submission(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('recipes:add'), {
            'name': '',  # Invalid empty name
            'cooking_time': -5,  # Invalid negative time
            'ingredients': '',
        })
        self.assertEqual(response.status_code, 200)  # Should not redirect, should return form errors
        self.assertFalse(Recipes.objects.filter(name='').exists())

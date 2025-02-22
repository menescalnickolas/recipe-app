from django.db import models
from django.shortcuts import reverse

# Create your models here.
difficulty_choice = (
    ('Easy', 'Easy'),
    ('Medium', 'Medium'),
    ('Intermediate', 'Intermediate'),
    ('Hard', 'Hard'),
)

class Recipes(models.Model):
  recipe_id = models.PositiveIntegerField()
  name = models.CharField(max_length=50)
  description = models.TextField()
  cooking_time = models.PositiveIntegerField(help_text='in minutes')
  ingredients = models.TextField()
  preparation_method = models.TextField()
  pic = models.ImageField(upload_to='recipes', default='no_picture.jpg')

  def __str__(self):
    return str(self.name)
  
  def get_absolute_url(self):
    return reverse ('recipes:detail', kwargs={'pk': self.pk})
  
  @property #Makes "difficulty" a computed attribute instead of storing it in the database. This means it updates dynamically.
  def difficulty(self):
    num_ingredients = len(self.ingredients.split(",")) 
    if self.cooking_time < 10 and num_ingredients < 4:
      return "Easy"
    elif self.cooking_time < 10 and num_ingredients >= 4:
      return "Medium"
    elif self.cooking_time >= 10 and num_ingredients < 4:
      return "Intermediate"
    else:
      return "Hard"
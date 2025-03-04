from django.db import models
from django.shortcuts import reverse
from cloudinary.models import CloudinaryField

# Create your models here.
difficulty_choice = (
    ('Easy', 'Easy'),
    ('Medium', 'Medium'),
    ('Intermediate', 'Intermediate'),
    ('Hard', 'Hard'),
)

class Recipes(models.Model):
  recipe_id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=50)
  description = models.TextField()
  cooking_time = models.PositiveIntegerField(help_text='in minutes')
  ingredients = models.TextField()
  preparation_method = models.TextField()
  pic = CloudinaryField('image')
  difficulty = models.CharField(
    max_length=20,
    choices=difficulty_choice,
    default='Easy'
    )

  def __str__(self):
    return str(self.name)
  
  def get_absolute_url(self):
    return reverse ('recipes:detail', kwargs={'pk': self.pk})
  
  
  def save (self, *args, **kwargs):
    num_ingredients = len(self.ingredients.split(",")) 
    if self.cooking_time < 10 and num_ingredients < 4:
      self.difficulty = "Easy"
    elif self.cooking_time < 10 and num_ingredients >= 4:
      self.difficulty = "Medium"
    elif self.cooking_time >= 10 and num_ingredients < 4:
      self.difficulty = "Intermediate"
    else:
      self.difficulty = "Hard"
    
    super().save(*args, **kwargs)  # Save the instance with the calculated difficulty
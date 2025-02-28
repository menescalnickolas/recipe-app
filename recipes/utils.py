from recipes.models import Recipes
from io import BytesIO 
import base64
import matplotlib.pyplot as plt
from django.db.models import Count 

def get_recipename_from_id(val):
  recipename=Recipes.objects.get(id=val)
  return recipename


def get_graph():
  buffer = BytesIO() #create a BytesIO buffer for the image
  plt.savefig(buffer, format='png') #create a plot with a bytesIO object as a file-like object. Set format to png
  buffer.seek(0) #set cursor to the beginning of the stream
  image_png=buffer.getvalue() #retrieve the content of the file
  graph=base64.b64encode(image_png) #encode the bytes-like object
  graph=graph.decode('utf-8') #decode to get the string as output
  buffer.close() #free up the memory of buffer
  return graph #return the image/graph

def get_chart(chart_type, data, **kwargs):
  plt.switch_backend('AGG')
  fig=plt.figure(figsize=(6,3))

  if chart_type == '#2':
    difficulty_counts = data.values('difficulty').annotate(count=Count('difficulty'))
    difficulty_labels = [count['difficulty'] for count in difficulty_counts]
    difficulty_values = [count['count'] for count in difficulty_counts]
    plt.pie(difficulty_values, labels=difficulty_labels, autopct='%1.1f%%', startangle=90)

  elif chart_type == '#1':
    if data.exists():
      recipe_names = [recipe.name for recipe in data]
      ingredient_counts = [len(recipe.ingredients.split(',')) for recipe in data]  # Assuming ingredients are a comma-separated string
      plt.bar(recipe_names, ingredient_counts)

  elif chart_type == '#3':
    cooking_times = [recipe.cooking_time for recipe in data]
    recipe_names = [recipe.name for recipe in data]
    plt.plot(recipe_names, cooking_times)

  else:
    print('Unknown chart type.')

  plt.tight_layout()
  chart =get_graph() 
  return chart    






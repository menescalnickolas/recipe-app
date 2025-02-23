from django.urls import path
from .views import home
from .views import RecipesListView
from .views import RecipeDetailView

app_name = 'recipes'

urlpatterns = [
   path('', home, name = 'home'),
   path('list/', RecipesListView.as_view(), name='list'),
   path('list/<pk>', RecipeDetailView.as_view(), name='detail')
]
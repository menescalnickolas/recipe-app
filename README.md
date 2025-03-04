# RECIPE APP
## Introduction
Welcome to the Recipe App, a Django-based web application designed to help users manage their own recipes. This app allows users to store recipe details, including cooking time, ingredients, and difficulty level.
The application is built using Django's robust framework, providing a structured database model, seamless migrations, and an easy-to-use interface for interacting with recipes.

## Features
- User Authentication: Users can log in and log out of the application to manage their recipe collection.
- Recipe Management: Users can add, view, and search recipes based on name, cooking time, ingredients, and difficulty.
- Charts and Filters: Users can filter recipes based on search queries and view recipe-related data in a chart format.
- About Me Page: A page displaying information about the developer.


## Installation
To set up the project, follow these steps:

### Clone the repository:
git clone <repository_url>
cd <project_directory>

### Create a virtual environment:
python -m venv venv
source venv/bin/activate  # For Windows, use `venv\Scripts\activate`

### Install the required dependencies:
pip install -r requirements.txt

### Apply migrations:
python manage.py migrate

### Create a superuser to log into the app:
python manage.py createsuperuser

### Run the development server:
python manage.py runserver

### Open the app in your browser:
http://127.0.0.1:8000

## Application Structure
### Views:

- login_view: Handles user login. Displays a login form and error messages if the login attempt fails.
- logout_view: Logs out the user and redirects to the success page.
- success: Displays a success message after a user logs out.
- about_me: Displays an 'About Me' page for the app creator.
- home: Displays the home page of the recipe section.
- RecipesListView: Displays a list of recipes, with optional search and chart filters.
- RecipeDetailView: Displays detailed information about a specific recipe.
- add_recipe: Allows users to add new recipes to the app.

### Models:

Recipes: Represents recipe data including name, cooking time, ingredients, and difficulty.


### Forms:

- RecipesSearchForm: A form to search recipes by different criteria.
- RecipeForm: A form for adding new recipes.

### Utilities:
- get_recipename_from_id: Utility function to get a recipe name from its ID.
- get_chart: Utility function to generate charts based on recipe data.


## URLs
- /auth/login/: User login page.
- /auth/logout/: User logout.
- /success/: A success message after logging out.
- /about_me/: Information about the app creator.
- /recipes/: A page listing all recipes.
- /recipes/add/: A form to add a new recipe.
- /recipes/<id>/: Detailed view of a specific recipe.

## Requirements
- Python 3.x
- Django 3.x or higher
- pandas
- matplotlib (for chart rendering)

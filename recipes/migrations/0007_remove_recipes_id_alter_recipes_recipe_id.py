# Generated by Django 4.2.19 on 2025-03-03 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_recipes_difficulty'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipes',
            name='id',
        ),
        migrations.AlterField(
            model_name='recipes',
            name='recipe_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

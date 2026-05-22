
from .models import Recipe, Category
from django.shortcuts import render
from django.db.models import Count
from .models import Category


def main(request):
    recipes = Recipe.objects.order_by('-created_at')[:5]

    return render(request, 'main.html', {
        'recipes': recipes
    })





def category_list(request):
    # Django зробить один оптимізований SQL-запит
    categories = Category.objects.annotate(recipe_count=Count('categories'))
    return render(request, 'category_list.html', {'categories': categories})
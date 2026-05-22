from django.shortcuts import render
from .models import Recipe, Category


def main(request):
    recipes = Recipe.objects.order_by('-created_at')[:5]

    return render(request, 'main.html', {
        'recipes': recipes
    })



def category_list(request):
    categories = Category.objects.all()

    category_data = []

    for category in categories:
        category_data.append({
            'name': category.name,
            'recipe_count': category.recipe_set.count()
        })

    return render(request, 'category_list.html', {
        'categories': category_data
    })

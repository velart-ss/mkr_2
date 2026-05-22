from django.test import TestCase
from django.urls import reverse
from .models import Category, Recipe

class RecipeViewsTestCase(TestCase):
    def setUp(self):
        # Створення тестових даних
        self.category = Category.objects.create(name="Desert")
        for i in range(6):  # Створюємо 6 рецептів, щоб перевірити обмеження в 5
            Recipe.objects.create(
                title=f"Recipe {i}",
                description=f"Description {i}",
                instructions=f"Instructions {i}",
                ingredients=f"Ingredients {i}",
                category=self.category
            )

    def test_main_view(self):
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main.html')
        # Перевірка, що на головній відображається рівно 5 рецептів
        self.assertEqual(len(response.context['recipes']), 5)

    def test_category_list_view(self):
        response = self.client.get(reverse('category_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'category_list.html')
        # Перевірка, чи передаються категорії в контекст
        self.assertIn('categories', response.context)
        # Перевірка, що анотація підрахунку працює (у нас 1 категорія з 6 рецептами)
        test_cat = response.context['categories'].first()
        self.assertEqual(test_cat.recipe_count, 6)
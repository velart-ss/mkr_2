from django.test import TestCase
from django.urls import reverse
from .models import Recipe, Category


class RecipeViewsTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(
            name='Desserts'
        )

        for i in range(7):
            Recipe.objects.create(
                title=f'Recipe {i}',
                category=self.category
            )


    def test_main_view_status_code(self):
        response = self.client.get(reverse('main'))

        self.assertEqual(response.status_code, 200)


    def test_main_view_template(self):
        response = self.client.get(reverse('main'))

        self.assertTemplateUsed(response, 'main.html')


    def test_main_view_contains_5_recipes(self):
        response = self.client.get(reverse('main'))

        recipes = response.context['recipes']

        self.assertEqual(len(recipes), 5)


    def test_category_list_status_code(self):
        response = self.client.get(reverse('category_list'))

        self.assertEqual(response.status_code, 200)


    def test_category_list_template(self):
        response = self.client.get(reverse('category_list'))

        self.assertTemplateUsed(response, 'category_list.html')
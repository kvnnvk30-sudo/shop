from decimal import Decimal

from django.test import TestCase
from django.urls import reverse

from .models import Item


class ItemModelTest(TestCase):
    def setUp(self):
        self.item = Item.objects.create(
            title="Тестовый товар",
            description="Описание тестового товара",
            price=Decimal("99.99"),
            is_available=True,
        )

    def test_str_returns_title(self):
        self.assertEqual(str(self.item), "Тестовый товар")

    def test_default_is_available_true(self):
        item = Item.objects.create(
            title="Другой товар",
            description="Описание",
            price=Decimal("10.00"),
        )
        self.assertTrue(item.is_available)

    def test_created_at_auto_set(self):
        self.assertIsNotNone(self.item.created_at)


class CatalogHomeViewTest(TestCase):
    def setUp(self):
        self.available_item = Item.objects.create(
            title="Доступный товар",
            description="Описание",
            price=Decimal("50.00"),
            is_available=True,
        )
        self.unavailable_item = Item.objects.create(
            title="Недоступный товар",
            description="Описание",
            price=Decimal("30.00"),
            is_available=False,
        )

    def test_home_page_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_page_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'catalog/index.html')

    def test_only_available_items_shown(self):
        response = self.client.get(reverse('home'))
        items = response.context['items']
        self.assertIn(self.available_item, items)
        self.assertNotIn(self.unavailable_item, items)
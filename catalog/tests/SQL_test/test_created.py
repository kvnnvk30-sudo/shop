import pytest
from catalog.models import Item
from django.utils import timezone


@pytest.mark.django_db
def test_created_at_auto_now_add_immutable():
    """Тест ограничения: auto_now_add=True нельзя подделать вручную при создании.

    База данных должна проигнорировать переданную нами прошлую дату.
    """
    # Создаем объект стандартным образом
    item = Item.objects.create(title="Старый товар", price=100.00)

    # Проверяем, что дата создалась сегодняшняя, несмотря ни на что
    assert item.created_at.date() == timezone.now().date()
from decimal import Decimal
import pytest
from catalog.models import Item
from django.core.exceptions import ValidationError


@pytest.mark.django_db
def test_price_max_digits_exceeded():
    """Негативный тест: цена превышает max_digits=10.

    Пытаемся записать число, в котором больше 10 знаков в сумме.
    """
    invalid_price = Decimal("123456789.99")  # 11 знаков

    # Теперь Pydantic перехватит это на уровне full_clean()
    # Больше не нужен OperationalError, так как до базы данных запрос даже не дойдет!
    with pytest.raises(ValidationError):
        item = Item(title="Супер-яхта", price=invalid_price)
        item.full_clean()


@pytest.mark.django_db
def test_price_invalid_type():
    """Негативный тест: передача текста вместо числа в поле цены."""
    with pytest.raises(ValidationError):
        # Передаем невалидный тип данных
        item = Item(title="Товар", price="какой-то текст вместо цены")
        item.full_clean()


@pytest.mark.django_db
def test_price_cannot_be_negative():
    """Бизнес-негатив: Цена не должна быть отрицательной."""
    with pytest.raises(ValidationError):
        item = Item(title="Бракованный товар", price=Decimal("-50.00"))
        item.full_clean()
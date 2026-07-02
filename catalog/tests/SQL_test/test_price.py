import pytest
from catalog.models import Item
from django.db import OperationalError
from decimal import Decimal
from django.core.exceptions import ValidationError



@pytest.mark.django_db
def test_price_max_digits_exceeded():
    """
    Негативный тест: цена превышает max_digits=10.
    Пытаемся записать число, в котором больше 10 знаков в сумме.
    """
    invalid_price = Decimal("123456789.99") 
    with pytest.raises((ValidationError, OperationalError)):
        item = Item(title="Супер-яхта", price=invalid_price)
        item.full_clean()
        item.save()


@pytest.mark.django_db
def test_price_invalid_type():
    """
    Негативный тест: передача текста вместо числа в поле цены.
    """
    with pytest.raises(ValidationError):
        item = Item(title="Товар", price="какой-то текст вместо цены")
        item.full_clean()


@pytest.mark.django_db
def test_price_cannot_be_negative():
    """
    Бизнес-негатив: Цена не должна быть отрицательной.
    """
    item = Item(title="Бракованный товар", price=Decimal("-50.00"))    
    with pytest.raises(ValidationError):
        item.full_clean()
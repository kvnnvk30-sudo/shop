from decimal import Decimal
from django.utils import timezone
from django.db import OperationalError
from django.core.exceptions import ValidationError
import pytest
from catalog.models import Item

# ==========================================
#  ТЕСТЫ ДЛЯ ПОЛЯ PRICE (DecimalField)
# ==========================================

@pytest.mark.django_db
def test_price_max_digits_exceeded():
    """
    Негативный тест: цена превышает max_digits=10.
    Пытаемся записать число, в котором больше 10 знаков в сумме.
    """
    # 9 знаков до запятой + 2 после = 11 знаков (лимит 10)
    invalid_price = Decimal("123456789.99") 
    
    with pytest.raises((ValidationError, OperationalError)):
        item = Item(title="Супер-яхта", price=invalid_price)
        # full_clean поймает это на уровне Django, а save() — на уровне базы
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


# ==========================================
#  ТЕСТЫ ДЛЯ ПОЛЯ IMAGE (ImageField)
# ==========================================

@pytest.mark.django_db
def test_image_blank_and_null_allowed():
    """
    Позитивный тест: проверяем, что поля blank=True и null=True
    разрешают оставлять картинку пустой.
    """
    item = Item.objects.create(title="Товар без фото", image=None)
    # В Django отсутствие файла проверяется через обычную проверку на ложность
    assert not item.image

# ==========================================
#  ТЕСТЫ ДЛЯ ПОЛЯ CREATED_AT (DateTimeField)
# ==========================================

@pytest.mark.django_db
def test_created_at_auto_now_add_immutable():
    """
    Тест ограничения: auto_now_add=True нельзя подделать вручную при создании.
    База данных должна проигнорировать переданную нами прошлую дату.
    """
    past_time = timezone.now() - timezone.timedelta(days=10)
    
    # Пытаемся принудительно засунуть в базу дату 10-дневной давности
    item = Item.objects.create(title="Старый товар", created_at=past_time)
    
    # Проверяем, что товар всё равно получил СЕГОДНЯШНЮЮ дату (с точностью до минуты)
    assert item.created_at.date() == timezone.now().date()


# ==========================================
#  БИЗНЕС-НЕГАТИВ (Логика приложения)
# ==========================================

@pytest.mark.django_db
def test_price_cannot_be_negative():
    """
    Бизнес-негатив: Цена не должна быть отрицательной.
    """
    item = Item(title="Бракованный товар", price=Decimal("-50.00"))
    
    # Теперь синтаксис правильный. Мы ожидаем, что full_clean() выбросит ValidationError
    with pytest.raises(ValidationError):
        item.full_clean()
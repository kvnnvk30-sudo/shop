import pytest
from catalog.models import Item


@pytest.mark.django_db
def test_image_blank_and_null_allowed():
    """Позитивный тест: проверяем, что поля blank=True и null=True

    разрешают оставлять картинку пустой.
    """
    item = Item.objects.create(title="Товар без фото", price=150.00, image=None)
    assert not item.image
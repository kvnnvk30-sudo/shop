from decimal import Decimal
import pytest
from playwright.sync_api import expect
from catalog.models import Item

pytestmark = [pytest.mark.django_db(transaction=True), pytest.mark.ui]


def test_catalog_empty_state(home_page):
    """Проверка пустой витрины."""
    Item.objects.all().delete()
    
    home_page.navigate()
    
    expect(home_page.get_empty_catalog_message()).to_be_visible()


def test_catalog_item_cards(home_page):
    """Проверка отображения карточек товаров и бэйджей."""
    item = Item.objects.create(title="Клавиатура", price=Decimal("100.00"), is_available=False)

    home_page.navigate()

    # Изолированная проверка внутри карточки конкретного товара
    card = home_page.get_product_card(item.title)
    expect(card).to_be_visible()
    expect(card.locator('p.text-muted')).to_contain_text(f"{item.price}")
    expect(card.locator('.badge')).to_have_text("Нет в наличии")
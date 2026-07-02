import pytest
from pydantic import ValidationError
from .models import ItemSchema 

def test_pydantic_valid_data():
    """Проверяем корректные данные"""
    data = {
        "title": "car",
        "price": 15.00,
        "is_available": True
    }
    item = ItemSchema(**data)  
    assert item.title == "car"
    assert item.price == 15.00

def test_pydantic_rejects_negative_price():
    """Проверяем, что отрицательная цена вызовет ошибку"""
    bad_data = {
        "title": "broken_car",
        "price": -500.00,
        "is_available": True
    }
    with pytest.raises(ValidationError) as exc_info:
        ItemSchema(**bad_data) 
    
    assert "price" in str(exc_info.value)

def test_pydantic_rejects_empty_title():
    """Проверяем, что пустое имя не пройдет"""
    bad_data = {
        "title": "",
        "price": 10.00
    }
    with pytest.raises(ValidationError):
        ItemSchema(**bad_data)
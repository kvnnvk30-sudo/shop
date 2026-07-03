from decimal import Decimal
from typing import Optional
from pydantic import BaseModel, Field, field_validator


class ItemSchema(BaseModel):
    title: str
    price: Decimal = Field(..., max_digits=10, decimal_places=2)
    image: Optional[str] = None
    is_available: bool = True  # Добавили поле в схему

    @field_validator("price")
    @classmethod
    def price_must_be_positive(cls, v: Decimal) -> Decimal:
        if v < 0:
            raise ValueError("Цена не должна быть отрицательной.")
        return v
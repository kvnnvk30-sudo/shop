from pydantic import BaseModel, Field

class ItemSchema(BaseModel):
    title: str = Field(min_length=1, max_length=255)
    price: float = Field(gt=0)
    is_available: bool = True
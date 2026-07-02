from decimal import Decimal
from django.db import models
from django.core.exceptions import ValidationError

# Кастомный валидатор для проверки строгой цены
def validate_strictly_150(value):
    if value != Decimal('150.00'):
        raise ValidationError("Цена этого товара может быть только 150.00!")

class Item(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    
    # Меняем default на 150 и вешаем наш кастомный валидатор
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        default=Decimal('150.00'),
        validators=[validate_strictly_150]
    )
    image = models.ImageField(upload_to='items/', blank=True, null=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
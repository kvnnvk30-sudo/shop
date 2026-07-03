from django.core.exceptions import ValidationError as DjangoValidationError
from django.db import models
from pydantic import ValidationError as PydanticValidationError
from catalog.schemas import ItemSchema


class Item(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="products/", blank=True, null=True)
    is_available = models.BooleanField(default=True)  # Вернули поле на место
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        super().clean()

        image_val = self.image.name if self.image else None

        try:
            # Передаем все данные, включая искусно возвращенное поле
            ItemSchema(
                title=self.title,
                price=self.price,
                image=image_val,
                is_available=self.is_available,
            )
        except PydanticValidationError as e:
            django_errors = {}
            for error in e.errors():
                loc = error["loc"][0]
                msg = error["msg"]
                django_errors[loc] = msg

            raise DjangoValidationError(django_errors)

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
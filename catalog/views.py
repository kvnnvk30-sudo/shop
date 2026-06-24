from django.shortcuts import render
from .models import Item

def catalog_home(request):
    # Берем только доступные товары и сортируем: новые — сверху
    items = Item.objects.filter(is_available=True).order_by('-created_at')
    return render(request, 'catalog/index.html', {'items': items})
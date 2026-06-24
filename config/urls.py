from django.contrib import admin
from django.urls import path
from catalog.views import catalog_home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', catalog_home, name='home'),  # Главная страница теперь ведет в магазин
]
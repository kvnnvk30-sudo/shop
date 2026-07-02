import pytest
from types import SimpleNamespace
from django.urls import reverse
from django.contrib.auth.models import User
from catalog.models import Item


@pytest.fixture
def home_response(client, db):
    User.objects.create_user(username='Nick', password='grop9302')
    Item.objects.create(title='car', price=15.00, is_available=True)
    return client.get(reverse('catalog:home'))

@pytest.fixture
def login_setup(client, db):
    user = User.objects.create_user(username='Nick', password='grop9302')
    response = client.get(reverse('catalog:login'))
    return SimpleNamespace(user=user, response=response, client=client)

@pytest.fixture
def logout_setup(client, db):
    user = User.objects.create_user(username='testuser', password='testpass123')
    client.login(username='testuser', password='testpass123')
    return SimpleNamespace(user=user, client=client)
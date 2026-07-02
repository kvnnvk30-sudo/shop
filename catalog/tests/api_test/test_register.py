from django.urls import reverse
from django.contrib.auth.models import User

def test_register_creates_user(client, db):
    response = client.post(reverse('catalog:register'), {
        'username': 'newuser',
        'email': 'new@test.com',
        'password1': 'ComplexPass123!',
        'password2': 'ComplexPass123!'
    })
    assert response.status_code == 302
    assert User.objects.filter(username='newuser').exists()
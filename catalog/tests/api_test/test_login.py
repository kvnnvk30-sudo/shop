from django.urls import reverse

def test_login_page_returns_200(login_setup):
    assert login_setup.response.status_code == 200
    
def test_login_with_correct_credentials(login_setup):
    response = login_setup.client.post(reverse('catalog:login'), {
        'username': login_setup.user.username,
        'password': 'grop9302'
    })
    assert response.status_code == 302

def test_login_with_wrong_password(login_setup):
    response = login_setup.client.post(reverse('catalog:login'), {
        'username': login_setup.user.username,
        'password': 'wrongpassword'
    })
    assert response.status_code == 200
    assert 'Неверный логин или пароль' in response.content.decode()
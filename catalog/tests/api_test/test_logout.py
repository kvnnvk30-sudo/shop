from django.urls import reverse

def test_logout_redirects(logout_setup):
    response = logout_setup.client.post(reverse('catalog:logout'))
    assert response.status_code == 302
    assert response['Location'] == reverse('catalog:home')
def test_home(home_setup):
    assert home_setup.response.status_code == 200 

def test_home_contains(home_setup):
    assert 'car' in home_setup.response.content.decode()

def test_home_uses_correct_template(home_setup):
    templates = [t.name for t in home_setup.response.templates]
    assert 'catalog/home.html' in templates
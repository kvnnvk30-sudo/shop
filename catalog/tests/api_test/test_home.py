def test_home_page_efficiency(home_response):
    """Проверяем статус-код, шаблон и контент главной страницы"""
    assert home_response.status_code == 200
    assert 'catalog/home.html' in [t.name for t in home_response.templates]
    assert 'car' in home_response.content.decode()
    
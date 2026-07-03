import pytest
from playwright.sync_api import expect
from django.contrib.auth.models import User

# Применяем маркеры на уровне модуля
pytestmark = [pytest.mark.django_db(transaction=True), pytest.mark.ui]


def test_successful_login(login_page):
    """Позитивный тест авторизации через POM."""
    User.objects.create_user(username="sdet_hero", password="password123")

    login_page.navigate()
    login_page.login("sdet_hero", "password123")

    # Проверяем состояние через элементы базовой страницы
    expect(login_page.navbar_text).to_contain_text("Привет, sdet_hero")
    expect(login_page.logout_button).to_be_visible()


def test_failed_login(login_page):
    """Негативный тест авторизации через POM."""
    login_page.navigate()
    login_page.login("hacker", "wrong_pass")

    error_alert = login_page.get_error_alert()
    expect(error_alert).to_be_visible()
    expect(error_alert).to_have_text("Неверный логин или пароль")
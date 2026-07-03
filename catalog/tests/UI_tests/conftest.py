import os
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
import pytest
from catalog.tests.UI_tests.pages import LoginPage, HomePage


@pytest.fixture(scope="function")
def login_page(page, live_server):
    """Фикстура для страницы логина."""
    return LoginPage(page, live_server.url)


@pytest.fixture(scope="function")
def home_page(page, live_server):
    """Фикстура для главной страницы."""
    return HomePage(page, live_server.url)
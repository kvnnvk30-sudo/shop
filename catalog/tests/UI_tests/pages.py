from playwright.sync_api import Page, expect

class BasePage:
    """Базовый класс для всех страниц приложения."""
    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url
        # Общие элементы для всех страниц (например, навбар из base.html)
        self.navbar_text = page.locator('.navbar-text')
        self.logout_button = page.locator('button:has-text("Выйти")')


class LoginPage(BasePage):
    """Страница авторизации (login.html)."""
    def navigate(self):
        self.page.goto(f"{self.base_url}/login/")

    def login(self, username, password):
        self.page.fill('input[name="username"]', username)
        self.page.fill('input[name="password"]', password)
        self.page.click('button:has-text("ВОЙТИ")')

    def get_error_alert(self):
        return self.page.locator('.alert-danger')


class HomePage(BasePage):
    """Главная страница каталога (home.html)."""
    def navigate(self):
        self.page.goto(self.base_url)

    def get_empty_catalog_message(self):
        return self.page.locator('p.text-muted', has_text="Товаров пока нет")

    def get_product_card(self, title: str):
        """Возвращает локатор конкретной карточки товара по его заголовку."""
        return self.page.locator('.card', has_text=title)
class ShopApiClient:
    """
    Обновленная «шапка». Теперь бьет по реальным путям твоего Django-приложения.
    """
    def __init__(self, locust_client):
        self.client = locust_client 

    def get_catalog(self):
        """Запрос на главную страницу каталога (путь '')"""
        return self.client.get("/", name="[Page] Home Catalog")

    def get_login_page(self):
        """Запрос на страницу авторизации (путь 'login/')"""
        return self.client.get("/login/", name="[Page] Login Page")
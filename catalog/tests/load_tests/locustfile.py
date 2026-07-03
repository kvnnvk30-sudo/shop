from locust import HttpUser, between
from catalog.tests.load_tests.clients.shop_client import ShopApiClient
from catalog.tests.load_tests.tasks.catalog_tasks import UserBehaviorTasks

class MarketProjectUser(HttpUser):
    # Время ожидания между шагами пользователя (от 1 до 3 секунд)
    wait_time = between(1, 3)
    tasks = [UserBehaviorTasks]

    def on_start(self):
        """
        Вызывается при старте виртуального пользователя.
        Инициализируем API-клиент и привязываем к пользователю.
        """
        self.api_client = ShopApiClient(self.client)

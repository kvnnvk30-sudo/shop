from locust import SequentialTaskSet, task

class UserBehaviorTasks(SequentialTaskSet):
    """
    Сценарий: зайти на главную, затем перейти на страницу логина.
    """
    
    @task
    def browse_shop(self):
        self.user.api_client.get_catalog()
        
    @task
    def open_login(self):
        self.user.api_client.get_login_page()
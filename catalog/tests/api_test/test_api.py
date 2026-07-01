from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from catalog.models import Item


class HomeViewTest(TestCase):
    def setUp(self):
        # Создаём тестового пользователя
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        # Создаём тестовый товар
        self.item = Item.objects.create(
            title='Тестовый товар',
            price=100.00,
            is_available=True
        )

    def test_home_returns_200(self):
        """Главная страница доступна без авторизации"""
        response = self.client.get(reverse('catalog:home'))
        self.assertEqual(response.status_code, 200)

    def test_home_contains_item(self):
        """На главной странице отображается товар из БД"""
        response = self.client.get(reverse('catalog:home'))
        self.assertContains(response, 'Тестовый товар')

    def test_home_uses_correct_template(self):
        """Главная использует правильный шаблон"""
        response = self.client.get(reverse('catalog:home'))
        self.assertTemplateUsed(response, 'catalog/home.html')


class LoginViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

    def test_login_page_returns_200(self):
        """Страница логина доступна"""
        response = self.client.get(reverse('catalog:login'))
        self.assertEqual(response.status_code, 200)

    def test_login_with_correct_credentials(self):
        """Успешный логин редиректит на главную"""
        response = self.client.post(reverse('catalog:login'), {
            'username': 'testuser',
            'password': 'testpass123'
        })
        self.assertRedirects(response, reverse('catalog:home'))

    def test_login_with_wrong_password(self):
        """Неверный пароль — остаёмся на странице логина"""
        response = self.client.post(reverse('catalog:login'), {
            'username': 'testuser',
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Неверный логин или пароль')


class RegisterViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_register_page_returns_200(self):
        """Страница регистрации доступна"""
        response = self.client.get(reverse('catalog:register'))
        self.assertEqual(response.status_code, 200)

    def test_register_creates_user(self):
        """Регистрация создаёт нового пользователя в БД"""
        response = self.client.post(reverse('catalog:register'), {
            'username': 'newuser',
            'email': 'new@test.com',
            'password1': 'ComplexPass123!',
            'password2': 'ComplexPass123!'
        })
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_register_redirects_after_success(self):
        """После регистрации — редирект на главную"""
        response = self.client.post(reverse('catalog:register'), {
            'username': 'newuser2',
            'email': 'new2@test.com',
            'password1': 'ComplexPass123!',
            'password2': 'ComplexPass123!'
        })
        self.assertRedirects(response, reverse('catalog:home'))


class LogoutViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

    def test_logout_redirects(self):
        """Выход редиректит на главную"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('catalog:logout'))
        self.assertRedirects(response, reverse('catalog:home'))
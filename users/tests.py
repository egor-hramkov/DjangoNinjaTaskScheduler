from django.contrib.auth.models import User
from django.test import TestCase, Client

class UserTests(TestCase):
    """Тесты для приложения пользователя"""
    BASE_URL = "/api/users/"
    c = Client()
    create_user_data = {
        "username": "test123",
        "email": "user@example.com",
        "first_name": "string",
        "last_name": "string",
        "password": "string"
    }

    def setUp(self):
        self.user_id = User.objects.create_user(username='test', password='test_password', email="test@mail.ru").id

    def test_get_user(self):
        """Тест на получение пользователя"""
        response = self.c.get(f"{self.BASE_URL}{self.user_id}")
        response_data = response.json()
        assert response.status_code == 200
        assert response_data['id'] == self.user_id

    def test_create_user(self):
        """Тест на создание пользователя"""
        response = self.c.post(self.BASE_URL, self.create_user_data, content_type="application/json")
        response_data = response.json()
        assert response.status_code == 200
        assert response_data['email'] == self.create_user_data['email']

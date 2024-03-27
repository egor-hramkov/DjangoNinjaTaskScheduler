from django.contrib.auth.models import User
from django.test import TestCase, Client

from ninja_jwt.tokens import AccessToken

from tasks.models import Task


class TaskTests(TestCase):
    """Тесты для раздела задач"""
    c = Client()
    BASE_URL = "/api/tasks/"

    def setUp(self):
        self.user = User.objects.create_user(username='test_for_task', password='abcdefasd', email="task@mail.ru")
        self.user_id = self.user.id
        self.task = Task.objects.create(name="test_task", description="teeeest", status='created', user=self.user)
        self.task_id = self.task.id
        self.token = AccessToken.for_user(self.user)
        self.task_data = {
            "name": "test_task",
            "description": "test_task",
            "status": "created",
        }

    def test_get_task(self):
        """Тест API на создание задачи"""
        response = self.c.get(f"{self.BASE_URL}{self.task_id}", HTTP_AUTHORIZATION=f'Bearer {self.token}')
        response_data = response.json()
        assert response.status_code == 200
        assert response_data['id'] == self.task_id

    def test_create_task(self):
        """Тест API на создание задачи"""
        response = self.c.post(
            f"{self.BASE_URL}",
            self.task_data,
            HTTP_AUTHORIZATION=f'Bearer {self.token}',
            content_type="application/json",
        )
        response_data = response.json()
        assert response.status_code == 200
        assert response_data['name'] == self.task_data['name']
        assert response_data['user']['id'] == self.user.id

    def test_update_task(self):
        """Тест API на обновление задачи"""
        ...

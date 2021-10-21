from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase

User = get_user_model()

API_URL = 'http://127.0.0.1:8000/api/v1.0/users'


class UserTests(APITestCase):
    def test_create_users(self):
        response = self.client.post(
            f'{API_URL}/create/',
            data={'first_name': 'user', 'last_name': 'test', 'password': 'passwordDefault1'}
        )
        self.assertEqual(response.status_code, 201)

    def test_list_users(self):
        response = self.client.get(f'{API_URL}/list/?page=1')
        self.assertEqual(response.status_code, 200)

    def test_friend_notifications(self):
        response = self.client.get(f'{API_URL}/friend-notifications/?')

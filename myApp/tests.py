from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()

class AuthTests(APITestCase):
    def setUp(self):
        self.signup_url = "/signup/"
        self.login_url = "/login/"
        self.user_data = {
            "username": "testuser",
            "password": "password123",
            "nickname": "tester",
            "birthday": "2000-01-01"
        }

    def test_signup(self):
        response = self.client.post(self.signup_url, self.user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login(self):
        User.objects.create_user(**self.user_data)
        response = self.client.post(self.login_url, {
            "username": "testuser",
            "password": "password123"
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)

    def test_access_private_service(self):
        User.objects.create_user(**self.user_data)
        login_response = self.client.post(self.login_url, {
            "username": "testuser",
            "password": "password123"
        })
        token = login_response.data["access"]

        response = self.client.get("/private/", HTTP_AUTHORIZATION=f"Bearer {token}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_access_private_service_without_login(self):
        response = self.client.get("/private/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

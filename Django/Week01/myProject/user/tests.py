from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from faker import Faker
from .models import User

fake = Faker()

# Create your tests here.
class UserSignUpTest(APITestCase):
    # setUp 함수를 이용해 test 실행 전 디폴트로 실행해줘도 ok
    def setUp(self):
        username = fake.user_name()
        email = fake.email()
        password = fake.password()

        self.user_data = {
            "username": username,
            "email": email,
            "password": password,
        }

    def testSignUp(self):
        url = reverse("sign_up")
        # 여기서 실행시켜줘도 ok
        # username = fake.user_name()
        # email = fake.email()
        # password = fake.password()

        # user_data = {
        #     "username": username,
        #     "email": email,
        #     "password": password,
        # }
        response = self.client.post(url, self.user_data)
        self.assertEqual(response.status_code, 200)

    def testSignIn(self):
        # 위에서 signup 을 해도 해당 데이터는 모듈이 끝나면 사라지게 된다
        # 따라서 새로 user 을 create 해줘야 하는데, sign up test 를 이미 완료했거나 필요하지 않은 경우 이를 setUp() 에서 처리할 수 있다
        self.user = User.objects.create_user(
            username=self.user_data["username"], 
            email=self.user_data["email"],
            password=self.user_data["password"]) 
        
        url = reverse("token_obtain_pair")
        
        response = self.client.post(url, self.user_data)
        self.assertEqual(response.status_code, 200)



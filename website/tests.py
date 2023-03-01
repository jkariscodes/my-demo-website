from django.contrib.auth.models import User
from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve

from .views import HomePageView


class HomePageTests(SimpleTestCase):
    def setUp(self):
        url = reverse("home")
        self.response = self.client.get(url)

    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_home_template(self):
        self.assertTemplateUsed(self.response, "website/home.html")

    def test_html_content(self):
        self.assertNotContains(self.response, "Habari yako!")

    def test_url_resolve_home(self):
        home_view = resolve("/")
        self.assertEqual(home_view.func.__name__, HomePageView.as_view().__name__)


class UserCreationTests(TestCase):
    user_name = "jkariukidev22"
    email = "jkariukidev22@email.com"
    password = "jkariuki123"

    def setUp(self):
        url = reverse("account_signup")
        self.response = self.client.get(url)

    def test_signup_form(self):
        user_one = User.objects.create_user(self.user_name, self.email, self.password)
        self.assertEqual(User.objects.all().count(), 1)
        self.assertEqual(User.objects.all()[0].username, self.user_name)
        self.assertEqual(User.objects.all()[0].email, self.email)

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class SignUpPageTests(TestCase):
    def test_url_exists_at_correct_location_signupview(self):
        response = self.client.get("/accounts/signup/")

        self.assertEqual(response.status_code, 200)

    def test_signup_view_name(self):
        response = self.client.get(reverse("signup"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "signup.html")

    def test_signup_form(self):
        response = self.client.post(
            reverse("signup"),
            {
                "username": "jkariukidev",
                "email": "jkariuki@email.com",
                "password1": "jkariuki123",
                "password2": "jkariuki123",
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(User.objects.all().count(), 1)
        self.assertEqual(User.objects.all()[0].username, "jkariukidev")
        self.assertEqual(User.objects.all()[0].email, "jkariuki@email.com")

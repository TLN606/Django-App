from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class AccountsTests(TestCase):
    def test_register_creates_user_and_logs_in(self):
        resp = self.client.post(reverse('register'), {
            'username': 'an', 'email': 'an@example.com',
            'password1': 'Mk-kho-doan-123', 'password2': 'Mk-kho-doan-123',
        })
        self.assertRedirects(resp, reverse('home'))
        self.assertTrue(User.objects.filter(username='an').exists())
        self.assertIn('_auth_user_id', self.client.session)

    def test_register_rejects_mismatched_passwords(self):
        resp = self.client.post(reverse('register'), {
            'username': 'an', 'password1': 'Mk-kho-doan-123', 'password2': 'khac',
        })
        self.assertEqual(resp.status_code, 200)
        self.assertFalse(User.objects.exists())

    def test_login_and_logout(self):
        User.objects.create_user('an', password='Mk-kho-doan-123')
        resp = self.client.post(reverse('login'), {'username': 'an', 'password': 'Mk-kho-doan-123'})
        self.assertRedirects(resp, reverse('home'))
        self.client.post(reverse('logout'))
        self.assertNotIn('_auth_user_id', self.client.session)

    def test_profile_requires_login(self):
        resp = self.client.get(reverse('profile'))
        self.assertRedirects(resp, f"{reverse('login')}?next={reverse('profile')}")

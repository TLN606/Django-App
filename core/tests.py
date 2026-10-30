from django.test import TestCase


class AdminSmokeTest(TestCase):
    def test_admin_login_page_loads(self):
        self.assertEqual(self.client.get('/admin/login/').status_code, 200)

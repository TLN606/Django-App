from django.test import TestCase

from menu.models import Category, Dish


class SmokeTest(TestCase):
    def test_admin_login_page_loads(self):
        self.assertEqual(self.client.get('/admin/login/').status_code, 200)

    def test_home_lists_available_dishes_only(self):
        cat = Category.objects.create(name='Cơm')
        Dish.objects.create(category=cat, name='Cơm tấm', price=45000)
        Dish.objects.create(category=cat, name='Cơm hết', price=40000, is_available=False)
        resp = self.client.get('/')
        self.assertContains(resp, 'Cơm tấm')
        self.assertNotContains(resp, 'Cơm hết')

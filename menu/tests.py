from io import StringIO

from django.core.management import call_command
from django.test import TestCase

from .models import Dish
from .templatetags.menu_extras import vnd


class SeedMenuTest(TestCase):
    def test_seed_is_idempotent(self):
        call_command('seed_menu', stdout=StringIO())
        count = Dish.objects.count()
        self.assertGreaterEqual(count, 10)
        call_command('seed_menu', stdout=StringIO())
        self.assertEqual(Dish.objects.count(), count)


class VndFilterTest(TestCase):
    def test_groups_thousands_with_dots(self):
        self.assertEqual(vnd(45000), '45.000')
        self.assertEqual(vnd('1250000'), '1.250.000')
        self.assertEqual(vnd(500), '500')

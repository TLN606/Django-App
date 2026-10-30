from io import StringIO

from django.core.management import call_command
from django.test import TestCase

from .models import Dish


class SeedMenuTest(TestCase):
    def test_seed_is_idempotent(self):
        call_command('seed_menu', stdout=StringIO())
        count = Dish.objects.count()
        self.assertGreaterEqual(count, 10)
        call_command('seed_menu', stdout=StringIO())
        self.assertEqual(Dish.objects.count(), count)

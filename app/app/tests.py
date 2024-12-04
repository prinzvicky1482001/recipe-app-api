from django.test import SimpleTestCase

from app import calc

class Test(SimpleTestCase):
    def test_subtract(self):
        res = calc.subtract(2, 3)
        self.assertEqual(res, 1)
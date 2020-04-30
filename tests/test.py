from unittest import TestCase
from teste import soma


class TestSoma(TestCase):

    def test_soma(self):
        self.assertEqual(soma(1, 2), 3)
